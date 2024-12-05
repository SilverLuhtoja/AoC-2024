def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("mul(")
    return content


def isNumberPair(nums):
    for num in nums:
        if not num.isnumeric():
            return False
    return True


def Solution1():
    data = get_filtered_data()
    result = 0

    for line in data:
        numbers = ""
        for char in line:
            if not char == ")":
                numbers += char
                continue
            break

        numbers = numbers.split(",")
        if isNumberPair(numbers):
            nums = [int(item) for item in numbers]
            result += nums[0] * nums[1]

    return result


def Solution2():
    data = get_filtered_data()
    result = 0
    isCalculationEnabled = True

    for line in data:
        numbers = ""
        for char in line:
            if not char == ")":
                numbers += char
                continue
            break

        numbers = numbers.split(",")
        if isNumberPair(numbers) and isCalculationEnabled:
            nums = [int(item) for item in numbers]
            result += nums[0] * nums[1]

        # enable/disable for next calculation
        if "don't()" in line:
            isCalculationEnabled = False
        if "do()" in line:
            isCalculationEnabled = True

    return result


# print(Solution1())
# print(Solution2())
