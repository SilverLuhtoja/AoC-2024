def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    return content


def isInBounds(pointer, box):
    return 0 <= pointer[1] < len(box[0]) and 0 <= pointer[0] < len(box)


SEARCH_PARAMETERS = [
    # forward
    [0, 1],
    # backwards
    [0, -1],
    # UPWARDS
    [-1, 0],
    # DOWNWARDS,
    [1, 0],
    # DIAGONALS,
    [1, 1],  # DOWN-RIGHT
    [1, -1],  # DOWN-LEFT
    [-1, 1],  # UP-LEFT
    [-1, -1]  # UP-RIGHT
]


def searchForChristmas(pointer, param, box):
    word = ""
    temp = pointer
    pointerList = [temp]
    for i in range(4):
        if not isInBounds(temp, box):
            return None
        word += box[temp[0]][temp[1]]
        temp = (temp[0] + param[0], temp[1] + param[1])
        pointerList.append(temp)

    return word


def searchForX(pointer, box):
    temp = pointer
    X_PARAMS = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
    letter = box[temp[0]][temp[1]]

    letters = []
    if letter == "A":
        for _, param in enumerate(X_PARAMS):
            temp = (temp[0] + param[0], temp[1] + param[1])
            if not isInBounds(temp, box):
                return False

            letter = box[temp[0]][temp[1]]
            if not letter in ["S", "M"]:
                return False

            temp = pointer  # set pointer back in middle
            letters.append(letter)

        first = letters[0] + "A" + letters[1]
        second = letters[2] + "A" + letters[3]
        return first in ["SAM", "MAS"] and second in ["SAM", "MAS"]

    return False


def Solution1():
    data = get_filtered_data()
    result = 0

    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            pointer = (i, j)
            for param in SEARCH_PARAMETERS:
                word = searchForChristmas(pointer, param, data)

                if word == "XMAS":
                    result += 1

    return result


def Solution2():
    data = get_filtered_data()
    result = 0

    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            pointer = (i, j)
            if searchForX(pointer, data):
                result += 1

    return result


# print(Solution1())
print(Solution2())
