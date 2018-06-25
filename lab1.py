import random

change = 1
i = 1

yes = 0
while i < 10:
    lst = [1, 2, 3]
    x = random.randint(1,4)
    n = random.randint(1,4)
    print("Set door {}".format(x))
    print("Choose door {}".format(n))
    for j in range(1,4):
        if j != x and j != n:
            k = lst.pop(lst.index(j))
            print("Remove door {}".format(k))
            break
    if change == 1:
        while True:
            s = random.choice(lst)
            if s != n:
                n = s
                break

    if n == x:
        yes += 1
    print(yes)
    i += 1
print(yes/10)