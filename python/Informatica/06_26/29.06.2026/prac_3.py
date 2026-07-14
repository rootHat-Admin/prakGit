# topic: Loop - while\for

task_list = ["Buy groceries", "Clean the room", "Reply to emails"]

while len(task_list) > 0:
    current_task = task_list.pop(0)
    print(f"Processing task: {current_task}")
    print(f"Tasks remaining: {len(task_list)}")

print("All tasks are done!")