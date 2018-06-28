#Task 1

# lst = [int(s) for s in input().split()]
# for i in lst:
#     if i % 2 != 0:
#         print(i, end = ' ')

#Task 2
# lst = [int(s) for s in input().split()]
# for i in range(0, len(lst)):
#     if lst[i] > lst[i-1]:
#         print(lst[i], end= ' ')

#Task 3
# lst = [int(s) for s in input().split()]
# for i in range(0, len(lst)):
#     if i % 2 == 0 and i != len(lst)-1:
#         lst[i],lst[i+1] = lst[i+1],lst[i]
#     print(lst[i], end=' ')

#Task 4
# lst = [int(s) for s in input().split()]
# m = min(lst)
# n = max(lst)
# lst[lst.index(m)],lst[lst.index(n)] = lst[lst.index(n)],lst[lst.index(m)]
# for i in lst:
#     print(i, end=' ')

#Task 5
# lst1 = [int(s) for s in input().split()]
# lst2 = [int(s) for s in input().split()]
# n = 0
# for i in lst1:
#     if i in lst2:
#         n += 1
# print(n)

#Task 6
# lst1 = [int(s) for s in input().split()]
# lst2 = [int(s) for s in input().split()]
# for i in lst1:
#     if i in lst2:
#         print(i, end=' ')

#Task 7
# lst1 = [int(s) for s in input().split()]
# lst2 = []
# for i in lst1:
#     if i in lst2:
#         print("Yes")
#     else:
#         print("No")
#         lst2.append(i)

#Tak 8
# s = input('Enter string')
# print(s[2])
# print(s[-1])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-1::-2])

#Task 9
# s = input('Enter string ')
# a = len(s)%2
# b = len(s) // 2
# s1 = s[:b+a]
# s2 = s[b+a:]
# print(s2+s1)

#Task 10
# s = input('Enter string ')
# print(s[:s.find('h')]+s[s.rfind('h')+1:])

#Task 11
# s = input('Enter string ')
# s1=s[:s.find('h')+1]
# s2 = s[s.find('h')+1:s.rfind('h')]
# s3 = s[s.rfind('h'):]
# print(s1+s2[::-1]+s3)

#Task 12
s = input('Enter string ')
s1=s[:s.find('h')+1]
s2 = s[s.find('h')+1:s.rfind('h')]
s2 = s2.replace('h', 'H')
s3 = s[s.rfind('h'):]
print(s1+s2+s3)