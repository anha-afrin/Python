class students:
    school_name="MCPSC"
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
        print("Student's Name: {} \nStudent's Grade: {} \nStudent's School Name: {}".format(self.name, self.grade, self.school_name))
student_1=students("Anha", 9)
student_2=students("Abrar", 3)
