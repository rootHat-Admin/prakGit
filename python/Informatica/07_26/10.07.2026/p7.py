print(f" {"Topic: Function - global"} ".center(90, "-"))

score = 0

def add_score():
    global score

    score += 10

add_score()
add_score()

print(score)
