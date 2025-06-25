#string indexing Slicing & methods

my_name="priyanka"
# index in postive
print(my_name[0])
print(my_name[1])
print(my_name[2])
print(my_name[3])
print(my_name[4])
print(my_name[5])
print(my_name[6])
print(my_name[7])

name3="hello World"
# negative index:
print(name3[-1])
print(name3[-2])
print(name3[-3])
print(name3[-4])
print(name3[-5])
print(name3[-6])
print(name3[-8])
print(name3[-9])
print(name3[-10])
print(name3[-11])

#string Slicing:

my_name= "priyanka"
# print(my_name1[0:3])

print(my_name[0:3])     # default step = 1
print(my_name[0:3:1]) 

print(my_name[0:5:1]) 

print(my_name[3:5:1]) 

print(my_name[0:5:2])   # step = 2

print(my_name[0:5:3])   # step = 3

print(my_name[0:5:4])   # step = 4 

print(my_name[0:2])        # first 2 chars
print(my_name[0:3])        # first 3 chars
print(my_name[2:5])        # third to fifth chars
print(my_name[1:4])        # second to fourth chars
print(my_name[-1:])        # last char of str
print(my_name[5:])         # last char of str
print(my_name[-2:])        # last 2 char of str
print(my_name[-3:])        # last 3 char of str
print(my_name[0::2])       # every second char
print(my_name[:])          # all char
print(my_name[::])         # all char 
print(my_name[::-1])       # reverse the string 


word = "Hello, Madhav" 

#1. len()
print(len(word)) 

#2. upper()
print(word.upper())

#3. lower()
print(word.lower())

#4. count()
print(word.count('M')) 

#5. find()
print(word.find('e'))

#6. Split()
print(word.split(','))
print(word.split()) 

#7. Replace()
print(word.replace("Madhav", "Keshav")) 

#8. title()
print(word.title()) 

#9. strip()
word2 = "  Hello World   "
print(len(word2))
print(word2.strip()) 

#10. join()
zwords = ("Madhav", "is", "Great")
print(" ".join(zwords))
print("-".join(zwords))