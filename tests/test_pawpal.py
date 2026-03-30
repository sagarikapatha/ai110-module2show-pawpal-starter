from datetime import datetime
from pawpal_system import Task, Pet


def test_task_mark_complete():
    task = Task(
        task_id="t1",
        title="Test Task",
        task_type="generic",
        scheduled_time=datetime.now(),
        priority=2,
        recurring=False,
        status="pending",
    )

    task.mark_complete()

    assert task.status == "completed"


def test_pet_add_task_increases_count():
    pet = Pet(
        pet_id="p1",
        name="Buddy",
        species="dog",
        age=3,
        breed="Labrador",
    )

    assert len(pet.tasks) == 0

    task = Task(
        task_id="t2",
        title="Feed Buddy",
        task_type="feeding",
        scheduled_time=datetime.now(),
        priority=1,
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task
