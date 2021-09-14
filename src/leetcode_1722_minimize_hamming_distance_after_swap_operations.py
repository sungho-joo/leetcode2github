# @l2g 1722 python3
# [1722] Minimize Hamming Distance After Swap Operations
# Difficulty: Medium
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations
#
# You are given two integer arrays,source and target,both of length n.
# You are also given an array allowedSwaps where each allowedSwaps[i] = [ai,
# bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source.
# Note that you can swap elements at a specific pair of indices multiple times and in any order.
# The Hamming distance of two arrays of the same length,source and target,
# is the number of positions where the elements are different.Formally,
# it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).
# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.
#
# Example 1:
#
# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
#
# Example 2:
#
# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
#
# Example 3:
#
# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# Output: 0
#
#
# Constraints:
#
# n == source.length == target.length
# 1 <= n <= 10^5
# 1 <= source[i], target[i] <= 10^5
# 0 <= allowedSwaps.length <= 10^5
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
#
#

from typing import Counter, DefaultDict, Dict, List


class union_find:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def ufind(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.ufind(self.parent[x])
        return self.parent[x]

    def uunion(self, a, b):
        ua = self.ufind(a)
        ub = self.ufind(b)
        self.parent[ua] = ub


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)

        uf = union_find(n)

        for x, y in allowedSwaps:
            uf.uunion(x, y)

        groups: DefaultDict[int, Dict[str, List[int]]] = defaultdict(lambda: {"s": [], "t": []})

        # grouping components by source's parent
        for i, val in enumerate(zip(source, target)):
            s: int = val[0]
            t: int = val[1]

            parent = uf.ufind(i)
            groups[parent]["s"].append(s)
            groups[parent]["t"].append(t)

        hamming_distance = 0

        for group in groups.values():
            hamming_distance += sum((Counter(group["s"]) - Counter(group["t"])).values())

        return hamming_distance


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1722.py")])
