def rate_func(current_command, info_plants):
    current_command, data = current_command.split(": ")
    plant_name, rating = data.split(" - ")
    rating = int(rating)
    if plant_name in info_plants:
        info_plants[plant_name]['Rating'].append(rating)
    else:
        print("error")
    return info_plants


def update_func(current_command, info_plants):
    current_command, data = current_command.split(": ")
    plant_name, new_rarity = data.split(" - ")
    if plant_name in info_plants:
        info_plants[plant_name]['Rarity'] = new_rarity
    else:
        print("error")

    return info_plants


def reset_plant_func(current_command, info_plants):
    current_command, plant_name = current_command.split(": ")
    if plant_name in info_plants:
        info_plants[plant_name]["Rating"] = []
    else:
        print("error")

    return info_plants


def store_information(num_of_plants):
    plants = {}

    for plant in range(num_of_plants):
        plant_info = input()
        plant, rarity = plant_info.split("<->")
        plants[plant] = {"Rarity": int(rarity), 'Rating': []}

    return plants


def print_func(info_plants):
    print("Plants for the exhibition:")
    for plant_name, info in info_plants.items():
        ratings = info['Rating']
        if ratings:
            average_rating = sum(ratings) / len(ratings)
            print(f"- {plant_name}; Rarity: {info['Rarity']}; Rating: {average_rating:.2f}")
        else:
            average_rating = 0
            print(f"- {plant_name}; Rarity: {info['Rarity']}; Rating: {average_rating:.2f}")


def main_func(num_of_plants):
    information = store_information(num_of_plants)

    command = input()

    while command != 'Exhibition':

        if command.startswith("Rate"):
            information = rate_func(command, information)
        elif command.startswith("Update"):
            information = update_func(command, information)
        elif command.startswith("Reset"):
            information = reset_plant_func(command, information)

        command = input()

    print_func(information)


number_of_plants = int(input())
main_func(number_of_plants)
