import streamlit as st

# Create a class
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_total(self):
        return self.m1 + self.m2 + self.m3

    def calculate_average(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"


# Streamlit UI
st.title("🎓 Student Marks Calculator (Using Class & Object)")

name = st.text_input("Enter Student Name")

marks1 = st.number_input("Enter Marks 1", min_value=0, max_value=100, step=1)
marks2 = st.number_input("Enter Marks 2", min_value=0, max_value=100, step=1)
marks3 = st.number_input("Enter Marks 3", min_value=0, max_value=100, step=1)

if st.button("Calculate Result"):
    
    # Create object
    student1 = Student(name, marks1, marks2, marks3)

    total = student1.calculate_total()
    average = student1.calculate_average()
    grade = student1.calculate_grade()

    st.subheader("📊 Result")
    st.write("Student Name:", student1.name)
    st.write("Total Marks:", total)
    st.write("Average Marks:", round(average, 2))
    st.write("Grade:", grade)
