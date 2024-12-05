import unittest
from unittest.mock import patch
from main import *


def mock_ReadFile(filepath):
    return """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


def mock_ReadFile2(filepath):
    return """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

class TestSolution(unittest.TestCase):

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution1()

        expected_result = 161

        self.assertEqual(result, expected_result)

    @patch('main.ReadFile', side_effect=mock_ReadFile2)
    def test_solution2(self, mock_ReadFile):
        result = Solution2()

        expected_result = 48

        self.assertEqual(result, expected_result)
