import streamlit as st

st.set_page_config(
    page_title="My Study Dashboard",
    page_icon="📚",
    layout="wide"
)

# Store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        "Practice Python",
        "Learn Object-Oriented Programming",
        "Practice NumPy and pandas",
        "Work on a Python project",
        "Practice Chinese"
    ]

# Title
st.title("📚 My Personal Study Dashboard")
st.write("Welcome back! Let's make today productive. ✨")

st.divider()

# Dashboard cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📖 Daily Study Goal", "4 Hours")

with col2:
    st.metric("📝 Total Tasks", len(st.session_state.tasks))

with col3:
    st.metric("🚀 Your Mission", "Keep Learning!")

st.divider()

# Add a new task
st.header("➕ Add a New Study Task")

with st.form("add_task_form"):
    new_task = st.text_input(
        "Enter your task",
        placeholder="e.g. Learn Machine Learning"
    )

    add_button = st.form_submit_button("Add Task")

    if add_button:
        if new_task.strip():
            st.session_state.tasks.append(new_task.strip())
            st.success("Your new task has been added! 🎉")
        else:
            st.warning("Please enter a task first.")

st.divider()

# Display tasks
st.header("📝 Today's Study Tasks")

completed = 0

for i, task in enumerate(st.session_state.tasks):
    if st.checkbox(task, key=f"task_{i}"):
        completed += 1

# Calculate progress
total_tasks = len(st.session_state.tasks)

if total_tasks > 0:
    progress = completed / total_tasks
else:
    progress = 0

st.divider()

# Progress bar
st.header("📊 Your Daily Progress")

st.progress(progress)

st.write(f"Completed: {completed} out of {total_tasks} tasks")
st.write(f"Progress: {int(progress * 100)}%")

if completed == total_tasks and total_tasks > 0:
    st.success("🎉 Amazing! You completed all your tasks!")
elif completed > 0:
    st.info("💪 Great progress! Keep going!")
else:
    st.write("🌱 Start with one small task today!")

st.divider()

# Choose a subject
st.header("🎯 What will you study today?")

subject = st.text_input(
    "Enter your subject",
    key="study_subject",
    placeholder="e.g. Python"
)

if st.button("Start Studying"):
    if subject.strip():
        st.success(f"🚀 Great! Time to study {subject}!")
    else:
        st.warning("Please enter a subject first.")

st.caption("Built with Python and Streamlit | Keep learning every day ❤️")