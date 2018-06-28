#Task 1
# s = input().split()
# d = {}
# for i in s:
#     n = d.get(i, 0)
#     print(n,end=' ')
#     d.update({i: n+1})

#Task 2
# d = {}
# n =int(input("Enter number of sinonims "))
# for i in range(0,n):
#     s = input().split()
#     d.update({s[0]: s[1]})
#     print(d)
# m = input("Enter key ")
# p=d.items()
# for i in p:
#     if m in i:
#         for j in i:
#             if j != m:
#                 print(j)

#Task 3
# d = {}
# n =int(input("Enter number of enters "))
# for i in range(n):
#     s = input().split()
#     m = d.get(s[0], 0)
#     d.update({s[0]: m+int(s[1])})
# lst = d.keys()
# for i in sorted(lst):
#     print(i, d.get(i))

#Task 4
# d = {}
# n =int(input("Enter number of enters "))
#
# for i in range(n):
#     s = input().split()
#     for j in s:
#         m = d.get(j, 0)
#         d.update({j: m+1})
# bigcount = 0
# words = []
# for word,count in d.items():
#     if count > bigcount:
#         words = []
#         words.append(word)
#         bigcount = count
#     elif count == bigcount:
#         words.append(word)
# print(sorted(words)[0])

#Task 5
# files = {}
# n_f =int(input("Enter number of enters "))
# for i in range(n_f):
#     file = input().split()
#     f = files.update({file[0]: file[1:]})
#
# operations = {'execute': "X", 'read': 'R', 'write': 'W'}
# n_o = int(input("Enter number of enters "))
# for i in range(n_o):
#     operation = input().split()
#     f = files.get(operation[1])
#     if operations[operation[0]] in f:
#         print('OK')
#     else:
#         print("DENIED")

#Task 6
# countries = {}
# n_c = int(input("Enter number of enters "))
# for i in range(n_c):
#     country = input().split()
#     f = countries.update({country[0]: country[1:]})
# cities = int(input("Enter number of enters "))
# for i in range(cities):
#     city = input()
#     for j in countries.items():
#         if city in j[1]:
#             print(j[0])

#Task 7
words = {}
n_w = int(input("Enter number of enters "))
for i in range(n_w):
    word = input().split()
    if len(word) > 1:
        for j in word:
            w = words.get(j, 0)
            words.update({j: w+1})
    # else:
    #     w = words.get(word, 0)
    #     words.update({word: w + 1})

a = sorted(words.items(), key=lambda x: x[1], reverse=True)
for i in a:
    print(i[0],i[1])
