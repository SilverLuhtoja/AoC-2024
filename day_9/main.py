def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip()
    return content


def create_file(input):
    id = 0

    file = []
    for idx, count in enumerate(input):
        if idx % 2 != 0:
            for i in range(int(count)):
                file.append(None)
        else:
            for i in range(int(count)):
                file.append(id)
            id += 1

    return file


def fill_empty_space(file):
    chars = list(file)
    n = len(chars)

    for i in range(n):
        if file[i] == None:
            for j in range(n - 1, i, -1):
                if file[j] != None:
                    file[i] = file[j]
                    file[j] = None
                    break

    return file


def get_check_sum(final_file):
    result = 0
    for i in range(len(final_file)):
        if final_file[i] != None:
            result += i * final_file[i]
    return result


def Solution1():
    data = get_filtered_data()
    file = create_file(data)
    final_file = fill_empty_space(file)

    return get_check_sum(final_file)


def getBiggestFileId(file):
    for i in range(len(file) - 1, 0, -1):
        if file[i] != None:
            return file[i]


def find_free_span(file, size):
    free_start = -1
    free_space_count = 0

    for i in range(len(file)):
        if file[i] is None:
            if free_start == -1:
                free_start = i
            free_space_count += 1
            if free_space_count == size:
                return free_start
        else:
            free_start = -1
            free_space_count = 0
    return None


def move_file_chunks(file):
    ID = getBiggestFileId(file)
    while ID > 0:
        file_size = file.count(ID)
        file_start_idx = file.index(ID)

        free_start = find_free_span(file[:file_start_idx], file_size)
        if free_start is not None:
            for i in range(file_size):
                file[free_start + i] = ID
                file[file_start_idx + i] = None

        ID -= 1

    return file


def Solution2():
    data = get_filtered_data()
    file = create_file(data)
    final_file = move_file_chunks(file)

    return get_check_sum(final_file)


# print(Solution1())
# print(Solution2())
