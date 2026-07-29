print(f" {"Topic: Function - Python_Files: .readlines()"} ".center(90, '-'))

f = open("data.txt")

lines = f.readlines()
print(lines[2])
f.close()