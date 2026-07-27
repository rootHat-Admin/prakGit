print(f" {"Topic: Function - Python_Files: .readlines()"} ".center(90, '-'))

with open("data.txt", "r") as f:
    lines = f.readlines()

print(lines)