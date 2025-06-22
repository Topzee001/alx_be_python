
# exercise 1

# creating a student class
class Student:
    def __init__(self, name, department, faculty):
        self.name = name
        self.department = department
        self.faculty = faculty
        self.level = 100 # default level

    def get_student_details(self):
        student_info = f"{self.name} is in {self.department} department, from the faculty of {self.faculty}"
        return student_info
    
    def student_level(self):
        print(f"the student is in {self.level} level")
    
    def promote_student(self, new_level):
        if new_level > self.level:
            self.level = new_level
        else:
            print("you can't go back to the previous level")

    
student_class = Student("Topzee", "Software Engineering", "Engineering and Technology")

print(student_class.get_student_details())

student_class.student_level()

student_class.promote_student(200)

student_class.student_level()

student_class.promote_student(300)

student_class.student_level()

student_class.promote_student(200)

student_class.student_level()



