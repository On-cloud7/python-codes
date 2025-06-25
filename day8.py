# #strings in python:

name= "priyanka1"
print(name)
print(type(name))

# formatted string - % Operator

name = "priyanka"
age = 16
print("my name is %s and i'm %d" % (name ,age))

 # formatted strings - str.format():

name = "priti"
age = 16
print("my name is {} and my age is {}" .format(name,age))

# # formatted strings - f strings

name = "sakshi"
age = 15
print(f"my name is {name} and im {age}")


# Escape Characters: backslash with chars


print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ")  # double quotes using \

print(" \'kw-single Quotes\' ") # single quote using \

print("Hello\nWorld")       # new line
print("Hello\tWorld") 



# String Operators in Python 
a = "Hello"
b = "Python"

print(a+b)      # concatenate 
print(a*2)      # multiple copies 
# [] - slice, [:] - range  -- scroll below

if "h" in a:
    print("Yess")
else:
    print("noo")

    
if "h" not in a:
    print("Yess")
else:
    print("noo") 

print(r"Hello\nWorld")  # Raw string: suppress the escape chars 

