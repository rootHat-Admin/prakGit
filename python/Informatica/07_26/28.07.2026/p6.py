print(f" {"Topic: Function - Python_Files: for line in f AND .readline()"} ".center(90, '-'))

f = open("data.txt")

print(f.readline())
print(f.readline())

for line in f:
    print(line)

f.close()