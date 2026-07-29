print(f" {"Topic: Function - Python_Files: .readlines()"} ".center(90, '-'))

f = open("data.txt")
lines = f.readlines()

for line in lines:
    print(line.strip())
    
f.close()