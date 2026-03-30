from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Tuple

@dataclass
class Task:
    task_id: str
    title: str
    task_type: str
    scheduled_time: datetime
    priority: int
    frequency: str = "none"
    status: str = "pending"

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.status = "completed"

    def update_task(self, **kwargs) -> None:
        """Update task attributes safely using a whitelist of editable fields."""
        editable_fields = {"title", "task_type", "scheduled_time", "priority", "frequency", "status"}
        for key, value in kwargs.items():
            if key in editable_fields:
                setattr(self, key, value)

    def is_conflicting(self, other: Task) -> bool:
        """Check if this task overlaps with another task in time."""
        return self.scheduled_time == other.scheduled_time

@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task_id: str) -> None:
        """Remove a task by ID."""
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def view_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    owner_id: str
    name: str
    contact_info: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_id: str) -> None:
        """Remove a pet by ID."""
        self.pets = [p for p in self.pets if p.pet_id != pet_id]

    def view_pets(self) -> List[Pet]:
        """Return all pets owned by this owner."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets owned by this owner."""
        return [task for pet in self.pets for task in pet.tasks]


@dataclass
class Scheduler:
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the scheduler."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets managed by this scheduler."""
        return [task for pet in self.pets for task in pet.tasks]

    def sort_tasks(self) -> List[Task]:
        """Sort tasks by priority (high first) then scheduled_time."""
        all_tasks = self.get_all_tasks()
        return sorted(all_tasks, key=lambda t: (-t.priority, t.scheduled_time))

    def sort_by_time(self) -> List[Task]:
        """Sort tasks by scheduled_time."""
        all_tasks = self.get_all_tasks()
        return sorted(all_tasks, key=lambda t: t.scheduled_time)
    
    def detect_conflicts(self) -> List[str]:
        """Return warning messages for tasks scheduled at the same time."""
        warnings = []
        all_tasks = self.get_all_tasks()

        for i, task1 in enumerate(all_tasks):
            for task2 in all_tasks[i + 1:]:
                if task1.scheduled_time == task2.scheduled_time:
                    pet1 = next((pet.name for pet in self.pets if task1 in pet.tasks), "Unknown")
                    pet2 = next((pet.name for pet in self.pets if task2 in pet.tasks), "Unknown")

                    warnings.append(
                        f"Conflict detected: '{task1.title}' for {pet1} and "
                        f"'{task2.title}' for {pet2} are both scheduled at "
                        f"{task1.scheduled_time.strftime('%Y-%m-%d %H:%M')}."
                    )
        return warnings

    def get_today_tasks(self) -> List[Task]:
        """Get all tasks scheduled for today."""
        today = datetime.now().date()
        return [t for t in self.get_all_tasks() if t.scheduled_time.date() == today]

    def filter_by_status(self, status: str) -> List[Task]:
        """Return tasks that match the given status."""
        all_tasks = self.get_all_tasks()
        return [task for task in all_tasks if task.status == status]

    def filter_by_pet_name(self, pet_name: str) -> List[Task]:
        """Return tasks for the pet with the given name."""
        matched_tasks = []
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower():
                matched_tasks.extend(pet.tasks)
        return matched_tasks
    
    def mark_task_complete(self, task: Task) -> None:
        """Mark a task complete and create the next recurring task if needed."""
        task.mark_complete()

        if task.frequency == "daily":
            next_time = task.scheduled_time + timedelta(days=1)
        elif task.frequency == "weekly":
            next_time = task.scheduled_time + timedelta(weeks=1)
        else:
            return

        new_task = Task(
            task_id=f"{task.task_id}_next",
            title=task.title,
            task_type=task.task_type,
            scheduled_time=next_time,
            priority=task.priority,
            frequency=task.frequency,
            status="pending",
        )

        for pet in self.pets:
            if task in pet.tasks:
                pet.add_task(new_task)
                break

