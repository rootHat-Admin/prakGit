print(f" {"20.08.2026"} ".center(90, '='))
print(f" {"Python_Practice_Exam | Topic: Basics | Exercise 3"} ".center(90, '-'))

enterMinutes  = int(input("Enter Minute: "))

sec = enterMinutes * 60
toHours = enterMinutes // 60 
toMinutes = enterMinutes % 60 

toDays = toHours // 24 
toDaysHours = toHours % 24 

toMonth = toDays // 30

print(f"Converts: Hours {toHours} : Minutes {toMinutes} : Second {sec}")
print(f"Converts: Days = {toDays} : Hours {toDaysHours} : Minutes {toMinutes} : Second {sec}")
print(f"Converts: Month = {toMonth} : Days {toDays} : Hours {toDaysHours} : Minutes {toMinutes} : Second {sec}")