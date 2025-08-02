# most asked question:

# 1.print the while loop output in same line:

# print("hello", end = " ")
# print("madhav")

# i = 1
# while i < 4:
#     print(f"Hello Madhav {i}",end = " ")
#     i +=1

# 2 print star patterns - using loops:

# Simple Triangle:
# n= 5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()


#inverted Triangle:

# n= 5
# for i in range (n, 0 ,-1):
#     for j in range (1 , i+1):
#         print("*", end = " ")
#     print()

#3. pyramid pattern :
n =5

# for i in range(1, n+1):
#     print(' ' * (n - i), end = "")
#     print("*" * (2 * i - 1))

# #find the factorial of a numbers:

# def fact(n):
#     result = 1
# #     while n >0 :
# #         result *= n
# #         n -=1
# #     return result
# # print(fact(5))

# #4 Count vowels in a string

# # my_string = "python by priyanka"
# # vowels = "aeiou"
# # count = 0

# # for char in my_string:
# #     if char.lower() in vowels:
# #         count += 1
# # print("number of vowels are ", count)

# # find the longest word in a string :

# sentence = "python by priyanka pardeshi"
# words = sentence.split()

# longest_word = ""

# for i in words:
#     if len(words) > len(longest_word):
#         longest_word = words
# print("the longest word is : ", longest_word)


#fibonacci sequence:

def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a)
        a,b = b , a+b
        count +=1
print(fibonacci(5))