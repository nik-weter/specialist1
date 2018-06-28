import random

def monty_hall(a):

    change = 1
    i = 1

    yes = 0
    while i < a:
        lst = [1, 2, 3]
        x = random.randint(1,4)
        n = random.randint(1,4)
        #print("Set door {}".format(x))
        #print("Choose door {}".format(n))
        for j in range(1,4):
            if j != x and j != n:
                k = lst.pop(lst.index(j))
                #print("Remove door {}".format(k))
                break
        if change == 1:
            while True:
                s = random.choice(lst)
                if s != n:
                    n = s
                    break

        if n == x:
            yes += 1
        i += 1
    return yes/a
l = monty_hall(1000)
print(l)