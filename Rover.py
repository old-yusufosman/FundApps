position = [0, 0, "N"]

def calculate_new_direction(facing, direction):
    combined = facing+direction
    direction_dictionary = {
        "NR": "E",
        "NL": "W",
        "ER": "S",
        "EL": "E",
        "SR": "W",
        "SL": "E",
        "WR": "N",
        "WL": "S",
    }

    return direction_dictionary.get(combined, "error")


def move_rover(direction):
    if direction == "F":
        return [0, position[1] + 1, "N"]
    elif direction == "B":
        return [0, position[1] - 1, "N"]
    elif direction == "L" or direction == "R":
        new_direction = calculate_new_direction(position[2], direction)
        return [0, position[1], new_direction]
