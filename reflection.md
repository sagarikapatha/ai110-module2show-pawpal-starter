# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.\
For PawPal+, I identified three main actions that users should be able to perform.\
First, a user should be able to add and manage pets. Since the system is focused on pet care, each owner needs a way to store information about their pets, such as the pet’s name, type, age, and other basic details.\
Second, a user should be able to schedule and track pet care tasks. These tasks may include feeding, walking, giving medication, or attending vet appointments. Each task should belong to a specific pet and include useful details such as date, time, priority, and whether it repeats.\
Third, a user should be able to view and organize daily tasks. The system should help owners quickly understand what needs to be done today by displaying tasks in a clear order, such as by time or priority. It should also support logic for identifying overlapping or conflicting tasks.

- What classes did you include, and what responsibilities did you assign to each?\
The initial UML design for PawPal+ focuses on four main classes: Owner, Pet, Task, and Scheduler. These classes represent the core components needed to manage pet care routines.

The **Owner** class represents the user of the system. It is responsible for storing basic owner information and maintaining a list of pets that belong to the owner. This allows the system to organize pet care tasks under a specific user.

The **Pet** class represents an individual pet. Each pet belongs to an owner and contains information such as the pet's name, type, and age. The Pet class also manages a list of tasks related to that pet, such as feeding, walking, or medication.

The **Task** class represents a care activity that needs to be performed for a pet. A task contains details such as the task name, scheduled time, priority level, and whether it repeats. This class is responsible for storing and updating task information.

The **Scheduler** class manages the organization of tasks. It is responsible for sorting tasks by time or priority, detecting scheduling conflicts, and retrieving tasks for a specific day. This class acts as the logic layer that helps keep the pet care schedule organized.

Together, these classes create a modular structure where owners manage pets, pets manage tasks, and the scheduler ensures tasks are organized efficiently.

**b. Design changes**

- Did your design change during implementation?\
Yes
- If yes, describe at least one change and why you made it.\
After reviewing my class skeleton with AI, I made an important design refinement to reduce ambiguity in task management. Initially, both the Pet class and the Scheduler class had responsibility for adding and storing tasks. This created a duplication problem because it was unclear whether tasks should live inside each pet or inside the scheduler.

To fix this, I made Pet the single source of truth for task storage. Each pet now owns its own list of tasks, and tasks are added through the Pet class. I updated the Scheduler design so that it works with a list of pets instead of maintaining a separate flat task list. This makes the Scheduler responsible only for organizing, sorting, and checking conflicts across pet tasks, rather than storing them.

I made this change because it creates a clearer separation of responsibilities, reduces data duplication, and makes conflict detection more meaningful by allowing tasks to be grouped by pet.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers several basic constraints when organizing pet care tasks. The main constraint is **scheduled time**, because tasks need to happen in a clear order throughout the day. It also considers **priority**, so more important tasks such as feeding, medication, or vet visits can be ranked above less urgent tasks. In addition, the scheduler uses **status** to separate pending tasks from completed ones, and it supports **frequency** so recurring daily or weekly tasks can automatically generate their next occurrence.

I decided that time and priority mattered most because they have the biggest impact on how a pet owner plans daily care. A task that is urgent but scheduled later still needs attention, while tasks that happen earlier should appear in the correct chronological order. Status and recurrence were also important, but they mainly support organization rather than deciding the main task order.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

My scheduler considers several basic constraints when organizing pet care tasks. The main constraint is **scheduled time**, because tasks need to happen in a clear order throughout the day. It also considers **priority**, so more important tasks such as feeding, medication, or vet visits can be ranked above less urgent tasks. In addition, the scheduler uses **status** to separate pending tasks from completed ones, and it supports **frequency** so recurring daily or weekly tasks can automatically generate their next occurrence.

I decided that time and priority mattered most because they have the biggest impact on how a pet owner plans daily care. A task that is urgent but scheduled later still needs attention, while tasks that happen earlier should appear in the correct chronological order. Status and recurrence were also important, but they mainly support organization rather than deciding the main task order.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
