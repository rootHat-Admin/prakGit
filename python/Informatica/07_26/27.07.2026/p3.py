print(f" {"Topic: Function - Python_Files: opening/closing"} ".center(90, '-'))

file = open("data.txt", "a")
file.write(" Python")
file.write("\nNew line")
file.close()