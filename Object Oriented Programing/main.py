class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print("The student's name is ",self.name)
        print("The student's age is ",self.age)
        # print("The teacher's name is ",self.name)
        # print("Tekson's age is ",self.age)
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
class Teacher(Person):
    def __init__(self, name, age, instituion, id):
        self.instituion=instituion
        self.id=id
        Person.__init__(self, name, age)
    def display3(self):
        print("Tekson is a professor at ", self.instituion)
        print("Tekson's id number is", self.id)
th=Teacher("Tekson", 49, "Harvard", 346710)
th.display()
th.display3()