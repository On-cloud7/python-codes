#write a python program to build a simple calculator
#Available Operations
# 1.Addition:
# 2.Subtraction:
# 3.Multiplication
# 4.Division:
# 5.Average :

#3 steps to build a calculator
# Functions for operations
# user input
# print result

#function to add two numbers

def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def mul(a,b):
    return (a*b)

def avg(a,b):
    return (a+b)/2

def divide (a,b):
    return(a/b)


#Step-2: user input 

print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n") 

select = int (input ("select a operation from 1, 2,3,4,5 : "))

number1 = int(input("enter first number :" ))
number2= int(input("enter second  number :" ))

#Step-3: Print the result 
if select == 1:
     print(number1, "+", number2, "= ", \
           add(number1, number2))
     
elif select == 2:
     print(number1, "-", number2, "= ", \
           sub(number1, number2)) 
     
elif select == 3:
     print(number1, "*", number2, "= ", \
           mul(number1, number2))
     
elif select == 4:
     print(number1, "/", number2, "= ", \
           avg(number1, number2))

elif select == 5:
     print("(",number1, "+", number2, ")", "/", "2", "= ", \
           divide(number1, number2)) 
    
else:
     print("Invalid operation! Pls select again!")
    