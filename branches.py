#Task 1
# n = int(input("Enter number "))
#
# if n%2 == 0:
#     print("Чет")
# else:
#     print("Нечет")

#Task 2
# n1 = int(input("Enter number 1 "))
# n2 = int(input("Enter number 2 "))
#
# print(min(n1,n2))


#Task 3
# n = int(input("Enter number "))
# if n > 0:
#     print(1)
# elif n<0:
#     print(-1)
# else:
#     print(0)

#Task 4
# n = int(input("Enter number "))
# if len(str(n)) == 3:
#     print("Да")
# else:
#     print("Нет")

# #Task 5
# n1 = int(input("Enter number 1 "))
# n2 = int(input("Enter number 2 "))
#
# if n1 > 0 and n2 > 0:
#     print("Да")
# elif n1 < 0 and n2 < 0:
#     print("Нет")

#Task 6
# n = input("Enter number ")
# if n[0] < n[1] and n[1] < n[2]:
#     print("Yes")
# else: print("No")

#Task 7
# n = input("Enter number ")
# if n == n[::-1]:
#     print("Yes")
# else: print("No")

# Task 8
# import calendar
# n = int(input("Enter month "))
# print(calendar.monthrange(2018, n)[1])

#Task 9
# n1 = input("Enter number 1 ")
# n2 = input("Enter number 2 ")
# n3 = input("Enter number 3 ")
# count = 0
# if n1 == n2 and n1 == n3:
#     count = 3
# elif n1 == n3 or n2 == n3:
#     count = 2
# elif n2 == n1:
#     count = 2
# print(count)

#task 10
# n1 = int(input("Enter number 1 "))
# n2 = int(input("Enter number 2 "))
#
# if n1%2 == 0 and n2%2 ==0:
#     print("Black")
# else:
#     print("White")

#Task 11
# def get_color(n1, n2):
#     if n1%2 == 0 and n2%2 ==0:
#         return "Black"
#     else:
#         return "White"
#
# n1 = int(input("Enter number 1 "))
# n2 = int(input("Enter number 2 "))
# n3 = int(input("Enter number 3 "))
# n4 = int(input("Enter number 4 "))
# if get_color(n1,n2) == get_color(n3,n4):
#     print("Yes")
# else: print("No")

#Task 12
# import datetime
# n1 = int(input("Enter number 1 "))
# n2 = int(input("Enter number 2 "))
# n = datetime.datetime(2018, n1, n2)
# delta = datetime.timedelta(1)
# n=n + delta
#
# print("{}-{}-{}".format(n.day, n.month, n.year))
