def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    return content


def method(line):
    pass


def Solution1():
    data = get_filtered_data()
    result = 0
    
    for line in data:
        result += method(line)

    return result


# def Solution2():
#      data = get_filtered_data()
#     result = 0

#     for line in data:
#         result += method(line)

#     return result


print(Solution1())
# print(Solution2())
