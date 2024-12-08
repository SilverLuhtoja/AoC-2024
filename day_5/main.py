import math


def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    updatePageNumbers = []
    pageOrderRulesMap = {}

    for item in content:
        if "" == item:
            continue

        if "|" in item:
            page, beforeOfPage = item.split("|")
            if page not in pageOrderRulesMap:
                pageOrderRulesMap[page] = [beforeOfPage]
            else:
                pageOrderRulesMap[page].append(beforeOfPage)
        else:
            updatePageNumbers.append(item)

    return pageOrderRulesMap, updatePageNumbers


def getMiddleNumber(line):
    middle = math.floor(len(line) / 2)
    return int(line[middle])


def isCorrectOrder(pages, numbers):
    for i, number in enumerate(numbers):
        beforeNrs = []
        if number in pages:
            beforeNrs = pages[number]
        for item in numbers[i+1:]:
            if item not in beforeNrs:
                return False
    return True


def orderNumbers(pages, numbers):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(numbers) - 1):
            left = numbers[i]
            right = numbers[i + 1]

            if right not in pages:
                continue

            if left in pages[right]:
                numbers[i], numbers[i + 1] = right, left
                sorted = False

    return numbers


def Solution1():
    pageOrderRulesMap, updatePageNumbers = get_filtered_data()
    result = 0

    for line in updatePageNumbers:
        splittedLine = line.split(",")
        if isCorrectOrder(pageOrderRulesMap, splittedLine):
            result += getMiddleNumber(splittedLine)

    return result


def Solution2():
    pageOrderRulesMap, updatePageNumbers = get_filtered_data()
    result = 0

    for line in updatePageNumbers:
        splittedLine = line.split(",")
        if not isCorrectOrder(pageOrderRulesMap, splittedLine):
            ordered = orderNumbers(pageOrderRulesMap, splittedLine)
            result += getMiddleNumber(ordered)

    return result


# print(Solution1())
print(Solution2())
