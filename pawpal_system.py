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
        pass

    def update_task(self, **kwargs) -> None:
        pass

    def is_conflicting(self, other: Task) -> bool:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass

    def view_tasks(self) -> List[Task]:
        pass


@dataclass
class Owner:
    owner_id: str
    name: str
    contact_info: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: str) -> None:
        pass

    def view_pets(self) -> List[Pet]:
        pass


@dataclass
class Scheduler:
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def sort_tasks(self) -> List[Task]:
        pass

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        pass

    def get_today_tasks(self) -> List[Task]:
        pass
