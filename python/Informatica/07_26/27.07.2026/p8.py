print(f" {"Topic: Function - Python_Files: .for line in f"} ".center(90, '-'))

with open("data.txt", "r") as f:
    lines = f.readlines()

print(lines[0])