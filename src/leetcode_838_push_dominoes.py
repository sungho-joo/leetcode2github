# @l2g 838 python3
# [838] Push Dominoes
# Difficulty: Medium
# https://leetcode.com/problems/push-dominoes
#
# There are n dominoes in a line,and we place each domino vertically upright.In the beginning,
# we simultaneously push some of the dominoes either to the left or to the right.
# After each second,each domino that is falling to the left pushes the adjacent domino on the left.
# Similarly,the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides,
# it stays still due to the balance of the forces.
# For the purposes of this question,
# we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:
#
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
#
# Return a string representing the final state.
#
# Example 1:
#
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
#
# Example 2:
#
#
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#
#
# Constraints:
#
# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] is either 'L', 'R', or '.'.
#
#

from typing import List


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def find_last_r(seg: List[str]) -> int:
            ind = -1
            for i in range(len(seg) - 1, -1, -1):
                if seg[i] == "R":
                    ind = i
                    break
            return ind

        segments, seg = [], []
        for domino in dominoes:
            seg.append(domino)
            if domino == "L":
                segments.append(seg)
                seg = []
        segments.append(seg)

        ans = []
        for seg in segments:
            if not seg:
                continue
            last_r = find_last_r(seg)

            # Before last R
            fall_r = False
            for i in range(last_r):
                if seg[i] == ".":
                    seg[i] = "R" if fall_r else "."
                elif seg[i] == "R":
                    fall_r = True

            # After last R to L
            # Last R, last L
            if last_r != -1 and seg[-1] == "L":
                l, r = last_r, len(seg) - 1
                while l < r:
                    seg[l] = "R"
                    seg[r] = "L"
                    l += 1
                    r -= 1
            # Last R, no L
            elif last_r != -1 and seg[-1] != "L":
                for i in range(last_r, len(seg)):
                    seg[i] = "R"
            # No R, last L
            elif last_r == -1 and seg[-1] == "L":
                seg = ["L"] * len(seg)
            # No R, No L
            else:
                pass

            ans.append("".join(seg))
        return "".join(ans)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_838.py")])
