def task_scheduling(tasks):
    tasks.sort(key=lambda x: x[1])  # Sort by end time
    print(tasks)
    selected_tasks = []
    last_end = 0
    for start, end in tasks:
        if start >= last_end:
            selected_tasks.append((start, end))
            last_end = end
    return selected_tasks

tasks = [(1, 3), (2, 5), (3, 9), (6, 8)]
print("Scheduled tasks:", task_scheduling(tasks))


'''
Task Scheduling Algorithm:

Definition: Select tasks based on their start and end times to complete the maximum number of non-overlapping tasks.
Objective: Schedule the maximum number of tasks without conflict.

Tasks: [(1, 3), (2, 5), (3, 9), (6, 8)]
Solution: [(1, 3), (6, 8)] (Select non-overlapping tasks)

'''