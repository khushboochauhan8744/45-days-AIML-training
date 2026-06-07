class Learner:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_info(self):
        return f"Learner Name: {self.name}, Course: {self.course}"


# Object creation
student = Learner("Khushbu", "Python Internship")

# Method call and output
print(student.get_info())