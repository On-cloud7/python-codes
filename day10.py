# #loops - for loop, while,for-each loop

# #while loop:

# count = 0 
# while count < 4:   #condition
#     print(count)
#     count +=1

# count = 5
# while count >0:
#     print(count)
#     count -=1
# else:
#     print("while loop ended")

# language = "python"
# for x in language:
#     print(x)

# # range(start)
# # range(start, stop)
# # range (start, stop, step)

# for i in range(5):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range (5):
#     print(i)
# else:
#     print("for loop ended")

# # loop control statements:
# # 1. pass statement:

# for i in range(5):
#     #mann nahi hai
#     pass

# count = 5
# while count > 0:
#     if count == 3:
#         pass
# else:
#     print(count)
# count -=1

# # 2.break statement:

# for i in range(10):
#     if i ==5:
#         break
#     print(i)

# # 3.continue statement:

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# while True:
#     user_input =input("enter the input ")
#     if user_input == "exit":
#         print("Congrats ! you guessed it right")
#         break
#     print("sorry, you entered:",user_input)


# #nested loops:
# # nested loop syntax:
# outer_loop:
#      inner_loop:
# #code - inner loop
# # code block to execute - outer loop



# # print numbers from 1 to 3:
# for i in range(3):
#     for num in range(1,4):
#         print (num)     
#     print("----------------------")


while i < 4:
    for j in range(1,4):
        print(j)
        print("----------------------")
        i +=1