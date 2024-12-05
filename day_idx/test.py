import unittest
from unittest.mock import patch
from main import *


def mock_ReadFile(filepath):
    return """x   x
x   x
"""


class TestSolution(unittest.TestCase):

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution1()

        expected_result = 0

        self.assertEqual(result, expected_result)

    # @patch('main.ReadFile', side_effect=mock_ReadFile)
    # def test_solution2(self, mock_ReadFile):
    #     result = Solution2()

    #     expected_result = 0

    #     self.assertEqual(result, expected_result)