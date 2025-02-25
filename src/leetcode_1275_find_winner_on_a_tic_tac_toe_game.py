# @l2g 1275 python3
# [1275] Find Winner on a Tic Tac Toe Game
# Difficulty: Easy
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game
#
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
# Here are the rules of Tic-Tac-Toe:
#
# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters,
# while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row,column,or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
#
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.
# Return the winner of the game if it exists (A or B),in case the game ends in a draw return "Draw",
# if there are still movements to play return "Pending".
# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe),
# the grid is initially empty and A will play first.
#
# Example 1:
#
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: "A" wins, he always plays first.
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"
#
# Example 2:
#
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: "B" wins.
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
# "   "    "   "    "   "    "   "    "   "    "O  "
#
# Example 3:
#
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
# "XXO"
# "OOX"
# "XOX"
#
# Example 4:
#
# Input: moves = [[0,0],[1,1]]
# Output: "Pending"
# Explanation: The game has not finished yet.
# "X  "
# " O "
# "   "
#
#
# Constraints:
#
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= moves[i][j] <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.
#

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check_winner(matrix):
            # Horizontal
            for i in range(3):
                if (matrix[i][0] == matrix[i][1] == matrix[i][2]) and (matrix[i][0] in [0, 1]):
                    return matrix[i][0]
            # Vertical
            for i in range(3):
                if (matrix[0][i] == matrix[1][i] == matrix[2][i]) and (matrix[0][i] in [0, 1]):
                    return matrix[0][i]
            # Diagonal
            if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] in [0, 1]:
                return matrix[0][0]
            if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[1][1] in [0, 1]:
                return matrix[1][1]
            return -1

        matrix = [[-1] * 3 for _ in range(3)]
        mark = 0
        for x, y in moves:
            matrix[x][y] = mark
            mark ^= 1
        res = check_winner(matrix)
        if res != -1:
            return "A" if res == 0 else "B"
        else:
            return "Draw" if len(moves) == 9 else "Pending"


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1275.py")])
