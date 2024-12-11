import math
from itertools import product


def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    answers, numbers = [], []
    for line in content:
        ans, nums = line.split(":")
        answers.append(int(ans))
        numbers.append([int(x) for x in nums.strip().split()])

    return answers, numbers


def calculate(operators, nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        if operators[i - 1] == "+":
            ans += nums[i]
        elif operators[i - 1] == "*":
            ans *= nums[i]
        else:
            ans = int(f"{ans}{nums[i]}")

    return ans


def Solution1():
    answers, numbers = get_filtered_data()
    correctValues = set()
    for i in range(len(answers)):
        for op in product("+*", repeat=len(numbers[i]) - 1):
            val = calculate(op, numbers[i])
            if val == answers[i]:
                correctValues.add(val)

    return sum(correctValues)


def Solution2():
    answers, numbers = get_filtered_data()
    correctValues = set()
    for i in range(len(answers)):
        for op in product("+*|", repeat=len(numbers[i]) - 1):
            val = calculate(op, numbers[i])
            if val == answers[i]:
                correctValues.add(val)

    return sum(correctValues)


# print(Solution1())
# print(Solution2())
