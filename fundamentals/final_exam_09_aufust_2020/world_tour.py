def add_stop_func(initial_str, command):
    data = command.split(':')
    index, added_stop = int(data[1]), data[2]
    if 0 <= index <= len(initial_str):
        initial_str = initial_str[:index] + added_stop + initial_str[index:]
    return initial_str


def remove_stop(initial_str, command):
    data = command.split(':')
    start_index, end_index = int(data[1]), int(data[2])
    if 0 <= start_index <= end_index <= len(initial_string):
        initial_str = initial_str[:start_index] + initial_str[end_index + 1:]
    return initial_str


def switch_func(initial_str, command):
    data = command.split(':')
    old_string, new_string = data[1], data[2]
    if old_string in initial_str:
        initial_str = initial_str.replace(old_string, new_string)

    return initial_str


def main_func(initial_str):
    while True:
        command = input()
        if command == 'Travel':
            return initial_str

        elif 'Add Stop' in command:
            initial_str = add_stop_func(initial_str, command)

        elif 'Remove Stop' in command:
            initial_str = remove_stop(initial_str, command)

        elif 'Switch' in command:
            initial_str = switch_func(initial_str, command)

        print(initial_str)


initial_string = input()
new_string = main_func(initial_string)
print(f"Ready for world tour! Planned stops: {new_string}")
