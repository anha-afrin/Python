class person:
    country="Bangladesh"
    def __init__(self, name, gender, age, profession, adress):
        self.name=name
        self.gender=gender
        self.age=age
        self.profession=profession
        self.adress=adress
        print("This person's name is: {} \nThis person's gender is: {} \nThis person's age is: {} \nThis person's profession is: {} \nThis person't country is: {} \nThis person's adress is: {}".format(self.name, self.gender, self.age, self.profession, self.country, self.adress ))
person_1=person("Anha", "Female", 15, "Student", "Dhaka_Mirpur_Pallabi")
person_2=person("Abrar","Male", 15, "Student", "Dhaka_Mirpur_Pallabi")
person_3=person("Oronno", "Male", 9, "Student", "Dhaka_Mirpur_Mallika")
person_4=person("Oishi", "Female", 19, "Student", "Dhaka_Mirpur_Mallika")
person_5=person("Sanjida", "Female", 24, "Banker", "Dhaka_Mirpur_Mallika")

        