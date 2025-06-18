#Assignment3 :

#condition1 : 4 divisible & 100 not divisible
#400 divisible

#user input

year = int(input("Enter the year(e.e 2024)"))

if (year % 4 == 0 and year %100 !=0) or \
      (year %400 == 0):
    print(f"{year} is leap year")
else:
    print("the year is not a leap yr")

# Q2:

# predefine username and password

predefined_username= '1'
predefined_password = '1'

username=input("enter the username : ")
password = input("enter the password : ")

if username == predefined_username:
    if password == predefined_password:
        print("Welcome login is successfull")
    else:
        print("incorrect password!")
else:
    print("invalid username")




# Q3:

Maths_marks = int(input("enter the marks of maths : "))
phy_marks = int(input ("Enter the marks of phys: "))
chem_marks = int(input("Enter the marks of chem"))

if (Maths_marks >= 65 and
    phy_marks >=55 and
    chem_marks >=50 and
    (Maths_marks+phy_marks+chem_marks) >=180 ) or \
    (Maths_marks+ phy_marks )>=140:
     print("you re eligible")
else:
    print("you are not eligible")
