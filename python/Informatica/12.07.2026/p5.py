print(f" {"Topic: Function - yield in Loops"} ".center(90, '-'))

def count():
    for i in range(5):
        yield i
    
for x in count():
    print(x)