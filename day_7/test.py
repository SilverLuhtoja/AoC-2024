import unittest
from unittest.mock import patch
from main import *


def mock_ReadFile(filepath):
    return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


class TestSolution(unittest.TestCase):

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution1()

        expected_result = 3749

        self.assertEqual(result, expected_result)

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution2(self, mock_ReadFile):
        result = Solution2()

        expected_result = 11387

        self.assertEqual(result, expected_result)
