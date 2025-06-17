#Data types in python

a=1
b=1
print(a)

print(a+b)

#basic data types in python:
#1. Numeric
 
a=1
b=1.5
print(type(b))
c=complex(3,5)
print(type(c))

#2. Sequence 

b1="priyanka"
print(type(b1))

b2 = [1,4,7,26,104,'priya'] #list
print(type(b2))

b3 = (2,4,6 ,'priya') #tuple
print(type(b3))

#3. Dictionary key-value pair

my_dictionary = {'name':'priyanka', 'age':'22','city': 'pune'}
print(type(my_dictionary))

# 4.sets

my_sets = {1,4,7,'priya'}
print(type(my_sets))

#5. Boolean

bool1= True
print(type(bool1))

#6. binary 
#bytes, bytearray,memoryview

byte1 = b"priyanka"
print(type(byte1))