import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner Information")
owner_name = st.text_input("Owner name", value="Jordan")

# Initialize session state objects
if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_id="o1", name=owner_name, contact_info="")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "pet_counter" not in st.session_state:
    st.session_state.pet_counter = 1

owner = st.session_state.owner
scheduler = st.session_state.scheduler
owner.name = owner_name

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Age", min_value=0, value=1)
breed = st.text_input("Breed", value="Unknown")

if st.button("Add Pet"):
    pet_id = f"p{st.session_state.pet_counter}"
    st.session_state.pet_counter += 1
    new_pet = Pet(pet_id=pet_id, name=pet_name, species=species, age=age, breed=breed)
    owner.add_pet(new_pet)
    scheduler.add_pet(new_pet)
    st.success(f"Added pet: {pet_name}")

st.subheader("Your Pets")
pets = owner.view_pets()
if pets:
    for pet in pets:
        st.write(f"- {pet.name} ({pet.species}, {pet.age} years old, {pet.breed})")
else:
    st.info("No pets added yet.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
