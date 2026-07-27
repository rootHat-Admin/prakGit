print(f" {"Topic: Function - Python_Files: Context Manager"} ".center(90, '-'))

with open("data.txt", "w") as f:
    f.write("Hello")

with open("data.txt", "r") as f:
    print(f.read())