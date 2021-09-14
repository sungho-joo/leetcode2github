# @l2g 1931 python3
# [1931] Painting a Grid With Three Different Colors
# Difficulty: Hard
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors
#
# You are given two integers m and n.Consider an m x n grid where each cell is initially white.
# You can paint each cell red,green,or blue.All cells must be painted.
# Return the number of ways to color the grid with no two adjacent cells having the same color.
# Since the answer can be very large,return it modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.
#
# Example 2:
#
#
# Input: m = 1, n = 2
# Output: 6
# Explanation: The six possible colorings are shown in the image above.
#
# Example 3:
#
# Input: m = 5, n = 5
# Output: 580986
#
#
# Constraints:
#
# 1 <= m <= 5
# 1 <= n <= 1000
#
#


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        states = []
        color_map = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
        MOD = 10 ** 9 + 7

        def get_states(arr, n):
            if n == m:
                states.append(arr)
            else:
                get_states(arr + [color_map[arr[-1]][0]], n + 1)
                get_states(arr + [color_map[arr[-1]][1]], n + 1)

        for i in range(3):
            get_states([i], 1)

        def check_adj(arr1, arr2):
            return all(elem1 != elem2 for elem1, elem2 in zip(arr1, arr2))

        adj_map = defaultdict(list)
        for i in range(len(states)):
            for j in range(len(states)):
                if check_adj(states[i], states[j]):
                    adj_map[tuple(states[i])].append(tuple(states[j]))

        @lru_cache(None)
        def dp(prev, N):
            if N == n:
                return 1

            ans = 0
            for next_state in adj_map[prev]:
                ans += dp(next_state, N + 1)
            return ans % MOD

        ret = 0
        for state in states:
            ret += dp(tuple(state), 1)

        return ret % MOD


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1931.py")])
