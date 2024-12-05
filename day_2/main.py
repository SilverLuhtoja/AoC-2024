def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    workableList = [item.split() for item in content]
    return [list(map(int, item)) for item in workableList]


data = get_filtered_data()


def is_safe(line) -> bool:
    isIncreasing = line[0] < line[1]

    for i, _ in enumerate(line):
        if i != len(line) - 1:
            difference = abs(line[i] - line[i + 1])
            if not 1 <= difference <= 3:
                return False

            if isIncreasing and line[i] > line[i + 1]:
                return False

            if not isIncreasing and line[i] < line[i + 1]:
                return False

    return True


def assure_safety(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        if is_safe(line[:i] + line[i+1:]):
            return True
    return False


def Solution1():
    result = 0
    for line in data:
        result += is_safe(line)

    return result


def Solution2():
    result = 0
    for line in data:
        result += assure_safety(line)

    return result


print(Solution1())
print(Solution2())
