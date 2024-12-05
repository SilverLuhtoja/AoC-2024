import unittest
from unittest.mock import patch
from main import *


def mock_ReadFile(filepath):
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


class TestSolution(unittest.TestCase):

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution1()

        expected_result = 2

        self.assertEqual(result, expected_result)

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution2()

        expected_result = 4

        self.assertEqual(result, expected_result)
