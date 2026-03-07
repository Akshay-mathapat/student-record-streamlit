import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Record System", page_icon="🎓", layout="wide")

st.title("🎓 Student Record Management System")
st.write("Manage student records and view academic performance")

# Store student data
if "students" not in st.session_state:
    st.session_state.students = []

# ----------------- TABS -----------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["➕ Add Student", "📋 View Students", "🔍 Search Student", "📊 Statistics"]
)

# ----------------- ADD STUDENT -----------------
with tab1:
    st.subheader("Add New Student")

    col1, col2 = st.columns(2)

    with col1:
        roll = st.text_input("Roll Number")
        name = st.text_input("Student Name")

    with col2:
        m1 = st.number_input("Marks 1", 0, 100)
        m2 = st.number_input("Marks 2", 0, 100)
        m3 = st.number_input("Marks 3", 0, 100)

    if st.button("Add Student"):
        avg = (m1 + m2 + m3) / 3

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "Roll Number": roll,
            "Name": name,
            "Marks1": m1,
            "Marks2": m2,
            "Marks3": m3,
            "Average": avg,
            "Grade": grade,
        }

        st.session_state.students.append(student)
        st.success("✅ Student Added Successfully!")

# ----------------- VIEW STUDENTS -----------------
with tab2:
    st.subheader("Student Records")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No students available")

# ----------------- SEARCH -----------------
with tab3:
    st.subheader("Search Student")

    roll_search = st.text_input("Enter Roll Number")

    if st.button("Search"):
        found = False
        for s in st.session_state.students:
            if s["Roll Number"] == roll_search:
                st.success("Student Found")
                st.json(s)
                found = True
                break

        if not found:
            st.error("Student not found")

# ----------------- STATISTICS -----------------
with tab4:
    st.subheader("Class Statistics")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Students", len(df))
        col2.metric("Highest Average", round(df["Average"].max(), 2))
        col3.metric("Class Average", round(df["Average"].mean(), 2))

        st.write("### Average Marks Chart")
        st.bar_chart(df.set_index("Name")["Average"])
# ----------------- STATISTICS -----------------
with tab4:
    st.subheader("Class Statistics")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Students", len(df))
        col2.metric("Highest Average", round(df["Average"].max(), 2))
        col3.metric("Class Average", round(df["Average"].mean(), 2))

        st.write("### Average Marks Chart")
        st.bar_chart(df.set_index("Name")["Average"])

        # -------- PIE CHART --------
        st.write("### Grade Distribution")

        grade_counts = df["Grade"].value_counts()

        fig, ax = plt.subplots()
        ax.pie(
            grade_counts,
            labels=grade_counts.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.axis("equal")

        st.pyplot(fig)

    else:
        st.warning("No data available")