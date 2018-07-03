import re


with open('train.txt', 'r') as f:
    with open('train_new.txt', 'w', encoding='utf-8') as f_new:
        for line in f:
            line = line.strip()
            #reg = re.match(r'([А-Яа-яЁё ]+)(\d{3})([\w ]*)([" из "|" в "])(\w+)([\d":"]{8})', line)
            reg = re.match('([А-Яа-яЁё ]+)(\d{3})([а-яё ]+)(из |в )([А-Яа-яЁё]+)([\w ]+)?(.{8}$)', line)
            if reg:
                line_new = "[{}]: Поезд номер {} {}{}{}".format(reg[7], reg[2], reg[4], reg[5],'\n')
                f_new.write(line_new)