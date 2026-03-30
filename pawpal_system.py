from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Tuple

@dataclass
class Task:
    task_id: str
    title: str
    task_type: str
    scheduled_time: datetime
    priority: int
    recurring: bool = False
    status: str = "pending"

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.status = "completed"

    def update_task(self, **kwargs) -> None:
        """Update task attributes safely using a whitelist of editable fields."""
        editable_fields = {"title", "task_type", "scheduled_time", "priority", "recurring", "status"}
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

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        """Find all conflicting tasks (same scheduled_time within same pet)."""
        conflicts = []
        for pet in self.pets:
            tasks = pet.tasks
            for i, task1 in enumerate(tasks):
                for task2 in tasks[i + 1:]:
                    if task1.is_conflicting(task2):
                        conflicts.append((task1, task2))
        return conflicts

    def get_today_tasks(self) -> List[Task]:
        """Get all tasks scheduled for today."""
        today = datetime.now().date()
        return [t for t in self.get_all_tasks() if t.scheduled_time.date() == today]

