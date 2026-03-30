from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(owner_id="o1", name="Ava", contact_info="ava@example.com")

    pet1 = Pet(pet_id="p1", name="Milo", species="dog", age=4, breed="Beagle")
    pet2 = Pet(pet_id="p2", name="Luna", species="cat", age=2, breed="Siamese")

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    now = datetime.now().replace(second=0, microsecond=0)
    task1 = Task(task_id="t1", title="Morning Walk", task_type="walk", scheduled_time=now + timedelta(hours=1), priority=3)
    task2 = Task(task_id="t2", title="Feed Breakfast", task_type="feeding", scheduled_time=now + timedelta(minutes=30), priority=2)
    task3 = Task(task_id="t3", title="Vet Check", task_type="vet", scheduled_time=now + timedelta(hours=2), priority=1)

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)

    scheduler = Scheduler()
    scheduler.add_pet(pet1)
    scheduler.add_pet(pet2)

    today_tasks = scheduler.get_today_tasks()

    print("Today's Schedule")
    print("=================")
    header = f"{'Time':<8} | {'Pet':<10} | {'Task':<20} | {'Priority':<8}"
    print(header)
    print('-' * len(header))

    for task in sorted(today_tasks, key=lambda t: (-t.priority, t.scheduled_time)):
        pet_name = next((pet.name for pet in scheduler.pets if task in pet.tasks), "Unknown")
        print(f"{task.scheduled_time.strftime('%H:%M'):<8} | {pet_name:<10} | {task.title:<20} | {task.priority:<8}")


if __name__ == '__main__':
    main()
