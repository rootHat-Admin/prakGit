print(f" {"Topic: Function - Python_Files: opening/closing"} ".center(90, '-'))

file = open("data.txt", "w")
file.write("Hello")
file.close()