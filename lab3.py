def read_file(name):
    lst = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lines = line.split()
            for i in lines:
                if i.lower() not in lst:
                    lst.append(i.lower())
    return lst
# a = read_file('data.txt')
# print(a)

def save_file(name, words):
    with open(name, 'w', encoding='utf8') as f:
        lst = sorted(words)
        f.write('Всего уникальных слов: {}\n'.format(len(lst)))
        for i in lst:
            f.write(i + '\n')

save_file('count.txt', read_file('data.txt'))