#input function

name=input("enter ur name")
print("my name is",name)

#write a program to input student name and marks ofsub print name and percentage

student_name1 = input("enter student name :""\n")
student_name2 = input("enter the student name2:""\n")
marks_stu1 =input("enter marks :""\n")
marks_stu2 = input("enter marks:""\n")
print("student 1 name is ",student_name1,"the student got marks",marks_stu1)
print("student 2 name is ",student_name2,"the student got marks",marks_stu2)

# Assignment - 2
# Write a program to input student name & marks of 3 subjects. 
# Print name & percentage in output. 

student_names= input("enter the name")
hindi_marks = int(input("enter the marks: "))
English_marks = int(input("enter the marks: "))
maths_marks = int(input("enter the marks: "))

percentage = (((hindi_marks)+(English_marks)+(maths_marks))/300)*100
print(f"The result of {student_names} is {int(percentage)}%. Well done!!")


# Q2: Write a program that collects multiple types of data to store in a dictionary 
# and print output.

#  initializing a dictionary
user_data = {} 

# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no)")

# print the input from user
print(user_data)