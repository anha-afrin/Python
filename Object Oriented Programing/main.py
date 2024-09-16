class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print("The student's name is ",self.name)
        print("The student's age is ",self.age)
class Student(Person):
    def __init__(self, name, age, grade, id):
        self.grade=grade
        self.id=id
        Person.__init__(self, name, age)
    def display2(self):
        print("The student's grade is ", self.grade)
        print("The student's id is ", self.id)
st=Student("Anha", 15, 9, 191213)
st.display()
st.display2()