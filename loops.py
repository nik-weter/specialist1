#Task 1
# n = int(input("Enter number "))
# x = 2
# while n%x > 0:
#     x+=1
# print(x)

#Task 2
# x = int(input("Enter number "))
# n = 1
# while (2 ** n) < x:
#     n+=1
# print(n-1, 2 ** (n-1))

#Task 3
# x = int(input("Enter number 1"))
# y = int(input("Enter number 2"))
# n = 1
# while x < y:
#     x += x/10
#     n += 1
# print(n)

#Task 4
# a = 0
# n = 0
# x = int(input("Enter number "))
# while x != 0:
#     if a == 0:
#         a = x
#     else:
#         if x > a:
#             n+=1
#     x = int(input("Enter number "))
# print(n)

#Task 5
# n = int(input("Enter number "))
# m = 1
# while m ** 2 <= n:
#     print(m**2, end=' ')
#     m += 1

#Task 6
#fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
# x = int(input("Enter number "))
# n=0
# a = 0
# l =[]
# while True:
#     n +=1
#     fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
#     l.append(fib(n))
#     if fib(n) >= x:
#         break
# if x in l:
#     print(l.index(x))
# else:
#     print(-1)

#Task 7
# n = int(input("Enter number "))
# def fib(n):
#     if n > 2:
#         return fib(n - 1) + fib(n - 2)
#     else:
#         return 1
# #fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
# print(fib(n))

#Task 8
s = 1
lst = []
x = int(input("Enter number "))
a = 0
n = 1
while x != 0:
    lst.append(x)
    if x == a:
        n += 1
    else:
        a = x
        if n > s:
            s = n
        n = 1
    x = int(input("Enter number "))
print(s)