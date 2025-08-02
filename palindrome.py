#palindrome String and number

# def palindrome(s):
#     temp = s[::-1]
#     if s == temp:
#         print("yes is is a palindrome")
#     else:
#         print("no ")
# s = "lol"
# palindrome(s)

#by using a for loop:

# def palindrome(s):
#     n = len(s)
#     for i in range(n):
#         if s[i] != s[n-i-1]:
#             return False
#         return True
# s= "lol"
# print(palindrome(s))

#while loop :
# def palindrome(s):
#     n = len(s)
#     first = 0
#     last = n-1
#     while(first< last):
#         if s [first]==s[last]:
#             first +1
#             last -=1
#         else:
#             return False
#         return True

# s = "priya"
# print(palindrome(s))


# palindrome by numbers:

# def palindrome(n):
#     temp = n
#     rev_n = 0
#     while(temp>0):
#         digit = temp % 10 #6
#         print(digit)
#         rev_n = rev_n *10 + digit
#         # rev_n = 0* 10 + 6 
#         temp = temp // 10
#     if n == rev_n:
#         return True
#     else:
#         return False
    
# n = 12345654321
# print(palindrome(n))

