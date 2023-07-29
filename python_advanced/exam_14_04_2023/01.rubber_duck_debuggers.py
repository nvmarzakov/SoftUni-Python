from collections import deque

time = deque(int(x) for x in input().split(" "))
number_of_tasks = deque(int(x) for x in input().split(" "))

collected_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time and number_of_tasks:
    current_tasks_time = time.popleft()
    current_number_of_task = number_of_tasks.pop()
    calculated_time = current_tasks_time * current_number_of_task

    if 0 <= calculated_time <= 60:
        collected_ducks["Darth Vader Ducky"] += 1

    elif 61 <= calculated_time <= 120:
        collected_ducks["Thor Ducky"] += 1

    elif 121 <= calculated_time <= 180:
        collected_ducks["Big Blue Rubber Ducky"] += 1

    elif 181 <= calculated_time <= 240:
        collected_ducks["Small Yellow Rubber Ducky"] += 1

    if calculated_time > 240:
        time.append(current_tasks_time)
        current_number_of_task -= 2
        number_of_tasks.append(current_number_of_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in collected_ducks.items():
    print(f"{key}: {value}")
