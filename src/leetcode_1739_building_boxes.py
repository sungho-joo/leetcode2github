# @l2g 1739 python3
# [1739] Building Boxes
# Difficulty: Hard
# https://leetcode.com/problems/building-boxes
#
# You have a cubic storeroom where the width,length,and height of the room are all equal to n units.
# You are asked to place n boxes in this room where each box is a cube of unit side length.
# There are however some rules to placing the boxes:
#
# You can place the boxes anywhere on the floor.
# If box x is placed on top of the box y,
# then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
#
# Given an integer n, return the minimum possible number of boxes touching the floor.
#
# Example 1:
#
#
# Input: n = 3
# Output: 3
# Explanation: The figure above is for the placement of the three boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.
#
# Example 2:
#
#
# Input: n = 4
# Output: 3
# Explanation: The figure above is for the placement of the four boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.
#
# Example 3:
#
#
# Input: n = 10
# Output: 6
# Explanation: The figure above is for the placement of the ten boxes.
# These boxes are placed in the corner of the room, where the corner is on the back side.
#
# Constraints:
#
# 1 <= n <= 10^9
#
#


class Solution:
    def minimumBoxes(self, n: int) -> int:
        # n <= 10^9, 2000th complete pyramid have more blocks than largest n
        complete_pyramid_list = [k * (k + 1) * (k + 2) / 6 for k in range(2000)]

        for i, value in enumerate(complete_pyramid_list):
            if n < value:
                largest_small_index = i - 1
                break
            elif n == value:
                return int(i * (i + 1) / 2)

        starting_pyramid_num = complete_pyramid_list[largest_small_index]

        self.fov = []
        self.fov_size = largest_small_index + 1
        self.fov.append([2000] * (self.fov_size + 1))
        for i in range(self.fov_size)[::-1]:
            cur_list = list(range(i + 1)[::-1])
            cur_list = [2000] + cur_list + [0] * (self.fov_size - len(cur_list))
            self.fov.append(cur_list)
        self.excess = 0

        for i in range(1, self.fov_size + 1):
            pos = [i, self.fov_size + 1 - (i)]
            self.fov[pos[0]][pos[1]] = 1
            self.excess += i

            if self.excess + starting_pyramid_num >= n:
                return int((self.fov_size - 1) * (self.fov_size) / 2) + i


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1739.py")])
