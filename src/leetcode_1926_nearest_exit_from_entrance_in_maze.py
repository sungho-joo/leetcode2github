# @l2g 1926 python3
# [1926] Nearest Exit from Entrance in Maze
# Difficulty: Medium
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze
#
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.
# ') and walls (represented as '+').You are also given the entrance of the maze,
# where entrance = [entrancerow,
# entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step,you can move one cell up,down,left,or right.You cannot step into a cell with a wall,
# and you cannot step outside the maze.Your goal is to find the nearest exit from the entrance.
# An exit is defined as an empty cell that is at the border of the maze.
# The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit,
# or -1 if no such path exists.
#
# Example 1:
#
#
# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.
#
# Example 2:
#
#
# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.
#
# Example 3:
#
#
# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.
#
#
# Constraints:
#
# maze.length == m
# maze[i].length == n
# 1 <= m, n <= 100
# maze[i][j] is either '.' or '+'.
# entrance.length == 2
# 0 <= entrancerow < m
# 0 <= entrancecol < n
# entrance will always be an empty cell.
#
#

from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])

        is_valid = lambda x, y: 0 <= x < n and 0 <= y < m and maze[x][y] == "."
        is_exit = lambda x, y: (x == 0 or x == n - 1 or y == 0 or y == m - 1) and not (
            [x, y] == entrance
        )
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # BFS
        q = deque()
        q.append([tuple(entrance), 0])
        while q:
            pos, move = q.popleft()
            if is_exit(*pos):
                return move
            for x, y in directions:
                new_pos = (pos[0] + x, pos[1] + y)
                if is_valid(*new_pos) and new_pos:
                    q.append([new_pos, move + 1])
                    maze[new_pos[0]][new_pos[1]] = "+"
        return -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1926.py")])
