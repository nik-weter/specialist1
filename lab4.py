
def read_nambers():

    filename = input('Enter filename ')
    with open(filename, 'r') as f:
        lst = []
        n = int(f.readline().strip())
        while n > 0:
            num = f.readline().strip()
            if len(num) == 0:
                raise EOFError('Need number!')
            if num.isdigit():
                lst.append(int())
            else:
                raise ValueError
            n -= 1
    print(lst)

try:
    read_nambers()
except FileNotFoundError:
    print("Enter true name!")
    read_nambers()
except PermissionError:
    print("You don't have permissions to access fot this file")
except ValueError:
    print("File have not numbers")
except EOFError:
    print("Too few nombers in file!")