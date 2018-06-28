import random

def birthday(j):
    k = 0
    n = 0
    while k < j:
        lst = []
        for i in range(0,23):
            lst.append((random.randint(1,29),random.randint(1,13)))
        for i in lst:
            if lst.count(i)>1:
                n+=1
                break
        k += 1
    return n/j
a = birthday(100000)
print(a)