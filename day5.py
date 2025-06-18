#Conditional Statements in python
 
# 1. if statement

a = 20
b = 29
if b>a:
    print("b is greater than a ")

age = int(input("enter the age : "))
if age > 19:
    print("you are an adult")

    

# 2. if-else condition :

temp = int(input(" enter the temperature : "))
if temp >25:
    print("it is hot day")
else:
    print("it is a cool day ")




# 3. if-elif-else condition:

score = int(input("enter ur score"))
if score >= 90:
    print("grade - A")
elif score >=80:
    print("grade - C")
elif score >=70:
    print("grade - D")
else:
    print("grade - D")



# 4. Nested 'if-else' Conditional :

number = int (input("enter ur number"))
if number > 0:
    if number %2 ==0:
        print("the number is positive and even")
    else:
        print("the number is positive and odd")
else:
    if number == 0:
        print("the number is zero")
    else:
        print("the number is negative")


# 5. Ternary Conditions:

age = int(input("enter ur age : "))
status = "adult" if age >=18 else "small"
print(status)