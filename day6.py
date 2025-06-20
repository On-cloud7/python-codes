# ##Functions in python:

# #create a function
# def greeting():
#     print("Welcome! to the python course by priyanka")

# #call Funtion (use funtion)

# greeting()

# #create a function to add 2 numbers

# def add2numbers(a,b): # parameters
#     result= a+b
#     print ("the sum is : " , result)

# #call function:

# add2numbers(5,7) #arguments

# ##return use kiya hai

# def add(a,b):
#     return a+b #after return statement function ends 

# result = add(3,6)
# print(result)


#function to covert celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#call function

temp_f = celsius_to_fahrenheit(25)
print(temp_f)