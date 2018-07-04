import csv


def get_books(s):
    with open('books.csv', "r") as f_obj:
        reader = csv.reader(f_obj, delimiter='|')
        lst = []
        for line in reader:
            for i in line:
                if s.lower() in i.lower():
                    lst.append(line)
    return lst

def get_totals(lst):
    res = []
    for i in lst:
        isbn = i[0]
        total = float(i[-1])*float(i[-2])
        if total < 500:
            total += 100
        res.append((isbn, total))
    return res
print(get_totals(get_books('python')))

