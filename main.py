from datetime import datetime, timedelta
from sched import scheduler
from pawpal_system import Owner, Pet, Task, Scheduler


def print_tasks(title, tasks, scheduler, show_pet=True):
    print(f"\n{title}")
    print("=" * len(title))
    if not tasks:
        print("No tasks found.")
        return

    if show_pet:
        header = f"{'Time':<18} | {'Pet':<10} | {'Task':<20} | {'Status':<10} | {'Priority':<8}"
    else:
        header = f"{'Time':<18} | {'Task':<20} | {'Status':<10} | {'Priority':<8}"

    print(header)
    print("-" * len(header))

    for task in tasks:
        time_str = task.scheduled_time.strftime("%Y-%m-%d %H:%M")
        if show_pet:
            pet_name = next((pet.name for pet in scheduler.pets if task in pet.tasks), "Unknown")
            print(f"{time_str:<18} | {pet_name:<10} | {task.title:<20} | {task.status:<10} | {task.priority:<8}")
        else:
            print(f"{time_str:<18} | {task.title:<20} | {task.status:<10} | {task.priority:<8}")


def main():
    owner = Owner(owner_id="o1", name="Ava", contact_info="ava@example.com")

    pet1 = Pet(pet_id="p1", name="Milo", species="dog", age=4, breed="Beagle")
    pet2 = Pet(pet_id="p2", name="Luna", species="cat", age=2, breed="Siamese")

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    now = datetime.now().replace(second=0, microsecond=0)

    task1 = Task(
        task_id="t1",
        title="Morning Walk",
        task_type="walk",
        scheduled_time=now + timedelta(hours=2),
        priority=3,
        frequency="none",
    )
    task2 = Task(
        task_id="t2",
        title="Feed Breakfast",
        task_type="feeding",
        scheduled_time=now + timedelta(hours=1),
        priority=2,
        frequency="none",
    )
    task3 = Task(
        task_id="t3",
        title="Vet Check",
        task_type="vet",
        scheduled_time=now + timedelta(minutes=30),
        priority=1,
        frequency="none",
    )
    daily_task = Task(
        task_id="t4",
        title="Daily Dinner",
        task_type="feeding",
        scheduled_time=now + timedelta(hours=4),
        priority=2,
        frequency="daily",
    )

    conflict_task = Task(
        task_id="t5",
        title="Lunch Feeding",
        task_type="feeding",
        scheduled_time=now + timedelta(hours=1),
        priority=2,
        frequency="none",
    )
    
    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)
    pet1.add_task(daily_task)
    pet2.add_task(conflict_task)

    task3.mark_complete()

    scheduler = Scheduler()
    scheduler.add_pet(pet1)
    scheduler.add_pet(pet2)

    scheduler.mark_task_complete(daily_task)

    print_tasks("All Tasks Sorted by Time", scheduler.sort_by_time(), scheduler)
    print_tasks("Tasks for Milo", scheduler.filter_by_pet_name("Milo"), scheduler)
    print_tasks("Completed Tasks", scheduler.filter_by_status("completed"), scheduler)
    print_tasks("Pending Tasks", scheduler.filter_by_status("pending"), scheduler)
    print_tasks("Milo Tasks After Completing Daily Task", scheduler.filter_by_pet_name("Milo"), scheduler)

    print("\nConflict Warnings")
    print("=================")
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No conflicts detected.")

if __name__ == "__main__":
    main()