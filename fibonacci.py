# # fibonacci series:

# def fibo(n):
#     a , b = 0,1
#     print(a)
#     while(b<n):
#         print(b)
#         c = a+b
#         a= b
#         b = c
    
# fibo(50)

# def fibo(n):
#     a , b = 0,1
#     print(a)
#     while(b<n):
#         print(b)
#         a ,b = b, a+b
    
# fibo(50)

# by using for loop:
def fibo (n):
    a,b = 0,1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b =c 
            print(c)
fibo(7)