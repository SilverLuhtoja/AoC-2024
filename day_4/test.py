import unittest
from unittest.mock import patch
from main import *


def mock_ReadFile(filepath):
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def mock_ReadFile2(filepath):
    return """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


class TestSolution(unittest.TestCase):

    @patch('main.ReadFile', side_effect=mock_ReadFile)
    def test_solution(self, mock_ReadFile):
        result = Solution1()

        expected_result = 18

        self.assertEqual(result, expected_result)

    @patch('main.ReadFile', side_effect=mock_ReadFile2)
    def test_solution2(self, mock_ReadFile):
        result = Solution2()

        expected_result = 9

        self.assertEqual(result, expected_result)
