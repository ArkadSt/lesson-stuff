# получить слово и название файла из списка апгументов (sys.argv)

# открыть файл

# прочитать файл построчно

# если слово есть в строке, вывести строчку на экран

# Обработать ошибку FileNotFoundError try-except

import sys
qwerty = sys.argv[1]
filename = sys.argv[2]
try:
    with open(filename, 'r' , encoding="utf-8") as file:
        for line in file:
            if qwerty in line:
                print(line)
except FileNotFoundError:
    print("file not found 404")