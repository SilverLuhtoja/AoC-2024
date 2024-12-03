import unittest
from unittest.mock import patch
from main import *


def mock_ReadFile(filepath):
    return """3   4
4   3
2   5
1   3
3   9
3   3"""


class TestSolution(unittest.TestCase):

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution1()

        expected_result = 11

        self.assertEqual(result, expected_result)

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution2()

        expected_result = 31

        self.assertEqual(result, expected_result)
