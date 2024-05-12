students_list = []
students_dict = {}

name = input ("Enter students name: ")
age = int(input("Enter students age:"))
grade = int(input("Enter studenrs grade:"))

students_list.append(name)
students_dict[name] = {"age":age, "grade":grade}
print(students_list )
print (students_dict)
print("Students information added sucessfully")

search_name = input ("Enter the name: ")
if search_student in students_list:
    print("students found!",students_dict)
else:
    print ("Student not found!")

remove_name = input("enter the name of the student")
if search_student in students_list:
    del students_dict[remove_name]
    students_list(remove_name)
else:
    print("student not found")
     
