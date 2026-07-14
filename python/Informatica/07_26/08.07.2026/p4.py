# 3. Scopes of visibility: global and nonlocal

# 2 - global

count = 0
def increment():
    global count
    count += 1
increment()
print(count) # 1