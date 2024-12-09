def ReadFile(file_name):
    return open(file_name, "r").read()


DIRECTIONS = {
    "LEFT": [0, -1],
    "RIGHT": [0, 1],
    "UP": [-1, 0],
    "DOWN": [1, 0]
}


def changeDirection(direction):
    if direction == "UP":
        return "RIGHT"
    elif direction == "RIGHT":
        return "DOWN"
    elif direction == "DOWN":
        return "LEFT"
    elif direction == "LEFT":
        return "UP"


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    return content


def isInBounds(pointer, box):
    return 0 <= pointer[1] < len(box[0]) and 0 <= pointer[0] < len(box)


def findGuardPosition(data):
    for row in range(len(data)):
        if "^" in data[row]:
            for col in range(len(data[row])):
                if "^" == data[row][col]:
                    return (row, col)
    return None


def getAllGuardLocations(guard_pos, data):
    FACING = "UP"
    seen = set()
    while True:
        velocity = DIRECTIONS[FACING]
        new_moving_pos = (guard_pos[0] + velocity[0],
                          guard_pos[1] + velocity[1])

        if not isInBounds(new_moving_pos, data):
            break

        moving_square = data[new_moving_pos[0]][new_moving_pos[1]]
        if moving_square == "#":
            FACING = changeDirection(FACING)
        else:
            guard_pos = new_moving_pos
            seen.add(new_moving_pos)
    return seen


def Solution1():
    data = get_filtered_data()
    guard_pos = findGuardPosition(data)
    return len(getAllGuardLocations(guard_pos, data))


def will_loop(starting_pos, oi, oj, data):
    if data[oi][oj] == "#":
        return False

    # for every loop, start from beginning
    i, j = starting_pos[0], starting_pos[1]
    data[oi][oj] = "#"  # add new obstacle for guard path
    FACING = "UP"

    seen = set()
    while True:
        if (i, j, FACING) in seen:
            data[oi][oj] = "."
            return True
        seen.add((i, j, FACING))

        velocity = DIRECTIONS[FACING]
        new_moving_pos = (i + velocity[0], j + velocity[1])
        if not isInBounds(new_moving_pos, data):
            data[oi][oj] = "."
            return False

        new_grid_value = data[new_moving_pos[0]][new_moving_pos[1]]
        if new_grid_value == "#":
            FACING = changeDirection(FACING)
        else:
            i, j = new_moving_pos[0], new_moving_pos[1]


def Solution2():
    data = get_filtered_data()
    starting_pos = findGuardPosition(data)
    visited_locations = getAllGuardLocations(starting_pos, data)

    result = 0
    data_list = [list(item) for item in data]
    for loc in visited_locations:
        result += will_loop(starting_pos, loc[0], loc[1], data_list)

    return result


print(Solution1())
print(Solution2())
