# topic: Loop - while\for

import time

seconds_left = 5

while seconds_left > 0:
    print(f"Time remaining: {seconds_left} seconds")
    time.sleep(1)
    seconds_left -= 1

print("Time is up! Launching...")