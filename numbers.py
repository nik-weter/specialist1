#Task 1
# n = int(input())
# n1 = n//10
# n2 = n%10
# print(n2, n1)

#Task 2
# n = int(input())
# n1 = n//10
# n2 = n%10
# n2 *= 10
# n = n2+n1
# print(n)

#Task 5
# n = int(input("Enter number: "))
# n1 = n//100
# n2 = (n-n1*100)//10
# n3 = (n-n1*100)%10
# print(n1 + n2 + n3)

#Task 6
# n = input("Enter number: ")
# print(n[n.find('.')+1])

#Task 7
# n = int(input("Enter number: "))
# if n % 100 == 0:
#     print(n // 100)
# else:
#     print((n // 100) + 1)

#Task 8
# n = int(input("Enter number: "))
# start = 4
# days = {0: "Воскресенье",1: "Понедельник",2: "Вторник",3: "Среда",4: "Четверг",5: "Пятница",6: "Суббота"}
# day = (n + start - 1) % 7
# print(days[day])

#Task 9
# n = int(input("Enter number: "))
# hours = n // 60
# minutes = n % 60
# print(hours, ':', minutes)

#Task 10
# a = int(input("Enter number of students in class a: "))
# b = int(input("Enter number of students in class b: "))
# c = int(input("Enter number of students in class c: "))
#
# def numbers(n):
#     if n % 2 == 0:
#         return n // 2
#     else:
#         return (n // 2) + 1
# print(numbers(a) + numbers(b) + numbers(c))

