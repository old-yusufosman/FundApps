grid_size = 100


def calculate_new_direction(facing, direction):
    combined = facing + direction
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
    return direction_dictionary.get(combined, "key {} not found".format(combined))


def calculate_new_position(position, direction):
    combined = position[2] + direction
    direction_dictionary = {
        "NF": [position[0], (position[1] + 1) % grid_size, position[2]],
        "NB": [position[0], (position[1] - 1) % grid_size, position[2]],
        "EF": [(position[0] + 1) % grid_size, position[1], position[2]],
        "EB": [(position[0] - 1) % grid_size, position[1], position[2]],
        "SF": [position[0], (position[1] - 1) % grid_size, position[2]],
        "SB": [position[0], (position[1] + 1) % grid_size, position[2]],
        "WF": [(position[0] - 1) % grid_size, position[1], position[2]],
        "WB": [(position[0] + 1) % grid_size, position[1], position[2]],
    }
    return direction_dictionary.get(combined, ["key {} not found".format(combined)])


class Rover:
    def __init__(self):
        self.position = [0, 0, "N"]

    def move_rover(self, direction):
        for char in direction:
            if char == "F" or char == "B":
                new_position = calculate_new_position(self.position, char)
                self.position = new_position

            elif char == "L" or char == "R":
                new_direction = calculate_new_direction(self.position[2], char)
                self.position = [self.position[0], self.position[1], new_direction]

        return self.position
