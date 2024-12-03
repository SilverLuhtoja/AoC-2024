from fileManager import ReadFile
import re


def sorted_lists():
    content = ReadFile("input.txt")
    matches = re.findall(r'\d+', content)

    list_1, list_2 = [], []
    cur_instance_nr = 0

    for letter in matches:
        if cur_instance_nr % 2 == 0:
            list_1.append(int(letter))
        else:
            list_2.append(int(letter))
        cur_instance_nr += 1

    list_1.sort()
    list_2.sort()

    return list_1, list_2


def Solution1():
    list_1, list_2 = sorted_lists()
    total_distance = 0
    for left, right in zip(list_1, list_2):
        total_distance += abs(left - right)

    return total_distance


def Solution2():
    list_1, list_2 = sorted_lists()
    similarity_score = 0

    for number in list_1:
        occurances = 0
        for number2 in list_2:
            if number == number2:
                occurances += 1
        similarity_score += number * occurances

    return similarity_score


def main():
    result = Solution2()
    print(result)


if __name__ == "__main__":
    main()
