🎓 Student Record Management System

A Streamlit-based web application for managing student records and performing basic academic analysis.
The system allows users to add students, search records, view class data, and visualize performance using charts.

Built with Python, Streamlit, pandas, and Matplotlib.

📌 Features

✔ Add new student records
✔ View all students in a table
✔ Search student by Roll Number
✔ Display class statistics
✔ Bar chart for student average marks
✔ Pie chart for grade distribution
✔ Clean and interactive web interface

🖥 Application Interface
Add Student

Users can enter:

Roll Number

Student Name

Marks for 3 subjects

The system automatically calculates:

Average marks

Grade (A, B, C, D, F)

View Students

Displays all student records in a structured table.

Search Student

Allows searching for a student using their Roll Number.

Class Statistics

Displays:

Total students

Highest average marks

Class average

Visualizations include:

📊 Bar chart of student averages

🥧 Pie chart showing grade distribution

🛠 Technologies Used

Python

Streamlit

pandas

Matplotlib

📂 Project Structure
student-record-streamlit
│
├── app.py
├── requirements.txt
└── README.md
⚙ Installation

Clone the repository:

git clone https://github.com/yourusername/student-record-streamlit.git

Navigate to the project folder:

cd student-record-streamlit

Install required dependencies:

pip install -r requirements.txt
▶ Running the Application

Start the Streamlit server:

streamlit run app.py

Then open your browser and go to:

http://localhost:8501
