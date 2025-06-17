#type casting in python:

a=1
print(type(a))

b="1"
print(type(b))

c=int(b)
print(type(c))

#all str values can't be casted into numerical type

#name="priyanka"
#newname = int(name)

print(a+int(b))
#all numerical type can be cast into str
mynum = 26
mynum2 = str(mynum)
print(type(mynum2))

f1 = 22.5
f2= int(f1)
print(type(f1))
print(type(f2))

f3= 7
f4= float(f3)
print(type(f4))


#implicit type casting
var1 = 10
var2 = 14.7
var3= var1+var2
print(var3)
print(type(var3))

#explicit type casting

int_num = 101
str_num = str(int_num)
print(type(str_num))