# @l2g 1769 python3
# [1769] Minimum Number of Operations to Move All Balls to Each Box
# Difficulty: Medium
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box
#
# You have n boxes.You are given a binary string boxes of length n,
# where boxes[i] is '0' if the ith box is empty,and '1' if it contains one ball.
# In one operation,you can move one ball from a box to an adjacent box.
# Box i is adjacent to box j if abs(i - j) == 1.Note that after doing so,
# there may be more than one ball in some boxes.
# Return an array answer of size n,
# where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
# Each answer[i] is calculated considering the initial state of the boxes.
#
# Example 1:
#
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations,
# and move one ball from the second box to the third box in one operation.
#
# Example 2:
#
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
#
# Constraints:
#
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.
#
#

from typing import Counter, List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box_map = Counter(boxes)
        ball_num = box_map["1"]

        moves = 0
        for ind, value in enumerate(boxes):
            if value == "1":
                moves += ind

        ans = [moves]

        prev_value = boxes[0]
        prev_balls = 0
        forward_balls = ball_num - int(boxes[0])
        prev_moves = moves
        for value in boxes[1:]:
            if prev_value == "0":
                prev_moves = prev_moves + prev_balls - forward_balls
            elif prev_value == "1":
                prev_moves = prev_moves + prev_balls + 1 - forward_balls
                prev_balls += 1
            ans.append(prev_moves)
            if value == "1":
                forward_balls -= 1
            prev_value = value

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1769.py")])
