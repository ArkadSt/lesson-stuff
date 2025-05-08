import sys

print(sys.argv)

file_path = sys.argv[1]  # input('Какой файл посмотреть' + '😏 ' + '? ')

try:
    with open(file=file_path, mode="r") as f:
        content = f.read()

    with open(file=file_path, mode="a") as f:
        f.write("\n\n" + content.replace("0", "o").replace("4", "a").replace("3", "e"))

except FileNotFoundError:
    print("File not found. Try different file name")

except PermissionError:
    print("File exists but you don't have permissions to access it.")
