# #function arguments:
# #1.required arguments:
# def greetings(name):  #name is a parameter
#     print("Hello "+name +"!")

# greetings("priyanka") # required an arguments to run code
 
# def intro(course_name , instructor_name):
#     print("welcome to  "+  course_name + " by  " + instructor_name)

# intro("python", "priyanka")

# #2. default argument:

# def greeting(name = "world"):
#     print("hello "+ name)

# greeting()   #default argument is used
# greeting("priyanka")


# # 3. keyword argument (named argument):

# def divide(a,b):
#     return a/b

# result1 = divide(100,20)  # positional argument
# print(result1 )

# result2 = divide(b=100,a=200) # keyword argument
# print(result2)


# # 4. arbitrary arguments(variable-length arguments *args and **kwargs):

# #arbitrary positional argument(*args)
# #**** Note:  stores arguments as tuples*****

# def add2numbers(a,b):
#     return a+b
# result = add2numbers(10,11)
# print(result)

# def add3numbers(a,b,c):
#     return a+b+c
# result2 = add3numbers(10,10,10)
# print(result2)


# def add_numbers(*args):
#     print(type(args))
#     return sum(args)

# op = add_numbers(90,90,89,67)
# print(op)

# #example 2:

# def greeting2(*name):
#     for names in name:
#         print(f"hello,{names}!")

# greeting2("priyanka","sakshi","aishu","prisha")

##arbitrary keywords arguments (**kwargs):

##  Note: the arguments are stored in dictionary ***

def print_details(**kwargs):
    print(type(kwargs))       # dictionary type
    for key, value in kwargs.items():
        print(f"{key}: {value}") 

# print_details(name = "Madhav", age = 26, city = "Delhi")

print_details(name = "Madhav", age = 26)