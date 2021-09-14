# @l2g 1706 python3
# [1706] Where Will the Ball Fall
# Difficulty: Medium
# https://leetcode.com/problems/where-will-the-ball-fall
#
# You have a 2-D grid of size m x n representing a box,and you have n balls.
# The box is open on the top and bottom sides.
# Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.
#
# A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
#
# We drop one ball at the top of each column of the box.
# Each ball can get stuck in the box or fall out of the bottom.
# A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.
# Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top,
# or -1 if the ball gets stuck in the box.
#
# Example 1:
#
#
# Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# Output: [1,-1,-1,-1,-1]
# Explanation: This example is shown in the photo.
# Ball b0 is dropped at column 0 and falls out of the box at column 1.
# Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
# Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
# Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
# Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
#
# Example 2:
#
# Input: grid = [[-1]]
# Output: [-1]
# Explanation: The ball gets stuck against the left wall.
#
# Example 3:
#
# Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
# Output: [0,1,2,3,4,-1]
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is 1 or -1.
#
#

from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def step(pos: List[int], pre_move: int):
            # end of row
            if pos[0] >= m:
                return pos[1] - 1

            # end of wall
            if walled_grid[pos[0]][pos[1]] == 2:
                return -1

            # moved left
            if pre_move == 0:
                if walled_grid[pos[0]][pos[1]] == 1:
                    return -1
                else:
                    output = step([pos[0] + 1, pos[1]], 2)
                    return output

            # moved right
            if pre_move == 1:
                if walled_grid[pos[0]][pos[1]] == -1:
                    return -1
                else:
                    output = step([pos[0] + 1, pos[1]], 2)
                    return output

            # moved down
            if pre_move == 2:
                if walled_grid[pos[0]][pos[1]] == 1:
                    output = step([pos[0], pos[1] + 1], 1)
                    return output
                else:
                    output = step([pos[0], pos[1] - 1], 0)
                    return output

        walled_grid = [[2] + column + [2] for column in grid]
        m = len(walled_grid)
        n = len(walled_grid[0])

        ans_list = [-1] * (n)
        for i in range(1, n - 1):
            print(f"{i}th ball")
            ans = step(pos=[0, i], pre_move=2)
            ans_list[i] = ans

        return ans_list[1:-1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1706.py")])
