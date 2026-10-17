
class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Course:", self.course)
        print("----------------------")


class StudentManagement:
    students = []

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

    @classmethod
    def display_all_students(cls):
        for student in cls.students:
            student.display_details()

    @classmethod
    def count_students(cls):
        return len(cls.students)


student1 = Student("ST001", "Amadu", "Computer Science")
student2 = Student("ST002", "Mohamed", "Information Technology")

StudentManagement.add_student(student1)
StudentManagement.add_student(student2)

StudentManagement.display_all_students()

print("Total Students:", StudentManagement.count_students())
