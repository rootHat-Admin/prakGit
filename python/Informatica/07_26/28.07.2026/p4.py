print(f" {"Topic: Function - Python_Files: for line in f"} ".center(90, '-'))

f = open("data.txt")

for line in f:
    print(line)

f.close()