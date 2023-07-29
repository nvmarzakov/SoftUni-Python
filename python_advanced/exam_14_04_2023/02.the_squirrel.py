def create_matrix(size):
    matrix = []
    squirrel_pos = []

    for i in range(size):
        row = list(input())
        matrix.append(row)

        if 's' in row:
            squirrel_pos = [i, row.index('s')]
            
    matrix[squirrel_pos[0]][squirrel_pos[1]] = '*'

    return matrix, squirrel_pos


def main_game_logic(created_matrix_and_sq_pos, list_moves):
    collected_hazelnuts = 0
    field, squirrel_pos = created_matrix_and_sq_pos[0], created_matrix_and_sq_pos[1]

    for index in range(len(moves)):
        command = list_moves[index]

        if command == 'down':
            squirrel_pos[0] += 1

        elif command == 'up':
            squirrel_pos[0] -= 1

        elif command == 'right':
            squirrel_pos[1] += 1

        elif command == 'left':
            squirrel_pos[1] -= 1

        if int(squirrel_pos[0]) == -1 or int(squirrel_pos[0]) > SIZE - 1:
            print("The squirrel is out of the field.")
            break
        elif int(squirrel_pos[1]) == -1 or int(squirrel_pos[1]) > (SIZE - 1):
            print("The squirrel is out of the field.")
            break

        if field[squirrel_pos[0]][squirrel_pos[1]] == 'h':
            field[squirrel_pos[0]][squirrel_pos[1]] = '*'

            collected_hazelnuts += 1

            if collected_hazelnuts == 3:
                print(f"Good job! You have collected all hazelnuts!")
                break

        if field[squirrel_pos[0]][squirrel_pos[1]] == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            break

    return f"Hazelnuts collected: {collected_hazelnuts}"


SIZE = int(input())
moves = input().split(", ")
matrix = create_matrix(SIZE)
print(main_game_logic(matrix, moves))
