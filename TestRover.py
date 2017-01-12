position = [0, 0, "N"]


def move_rover(direction):
    if direction == "F":
        return [0, position[1] + 1, "N"]
    elif direction == "B":
        return [0, position[1] - 1, "N"]
