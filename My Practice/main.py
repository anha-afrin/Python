# List
students_list=["Anha", "Abrar", "Aurthy", "Oronno"]
print(students_list)
students_list.append("Omni")
print(students_list)
students_list.remove("Omni")
print(students_list)
students_list.reverse()
print(students_list)
students_list.pop(0)
print(students_list)
# Dictionary
students_info={"Name": "Anha", "Age": 15, "Gender": "Female", "School": "MCPSC"}
print(students_info)
print(students_info["Gender"])
students_info["Sibling"]=1
print(students_info)
students_info["Club"]="Debate"
print(students_info)
students_info["Club"]="Science"
print(students_info)
students_info.pop("Sibling")
print(students_info)
# Set
students_bmi={22.23, 14.37, 19.21, 25.84}
print(students_bmi)
Others={78.90, 34.6, 22.23, 19.21}
print(Others)
inter=students_bmi.intersection(Others)
print(inter)
uni=students_bmi.union(Others)
print(uni)
print(students_bmi.symmetric_difference(Others))
students_bmi.add(66.55)
print(students_bmi)
# Tupple
tititutu=("Tensor", 9.8, 20, "Vector")
print(tititutu)
print(tititutu[0])