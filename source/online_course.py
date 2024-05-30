class OnlineCourse:
    def __init__(self, course_name: str, instructor: str) -> None:
        self.course_name: str = course_name
        self.instructor: str = instructor
        self.student_enrollment = []

    def add_student(self, student: object) -> None:
        self.student_enrollment.append(student)
        print(
            f"student name: {student.student_name}\nhas been enrolled in {self.course_name}".title()
        )

    def get_course_details(self):
        print(
            f"""
Course name: {self.course_name}
Instructor name: {self.instructor}
student:
    {self.student_enrollment}
            """
        )

    def completed_course(self, name):
        for student in self.student_enrollment:
            if name in student.student_name:
                self.student_enrollment.remove(student)
                print(f"{name} has completed this course".title())
            else:
                print(f"{name} has not enrolled in the course".title())

    def avg_grade(self, student: object):
        total = sum(student.grades)
        avg_grade = total / len(student.grades)
        print(f"the average Grade: {avg_grade:.3f}")


"""use this class as data base"""


class Student:
    def __init__(self, student_name, grades) -> None:
        self.student_name = student_name
        self.grades = grades


if __name__ == "__main__":
    python_course = OnlineCourse(
        "Object Oriented Programming In Python", "Me Ya Ro7 Omk"
    )

    num_of_students = int(input("enter the number of student: ".title()))

    for _ in range(num_of_students):
        student = input("student name: ").strip().lower()
        grade = []
        for _ in range(3):
            student_grades = int(input("input your grade: ").strip())
            grade.append(student_grades)
        student_ = Student(student_name=student, grades=grade)
        python_course.add_student(student_)
        python_course.avg_grade(student_)
        python_course.completed_course(student_.student_name)
