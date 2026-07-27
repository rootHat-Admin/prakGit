print(f" {"Topic: Function - Python_Files: readline"} ".center(90, '-'))

with open("data.txt", "r") as f:
    line = f.readline()
    print(line)