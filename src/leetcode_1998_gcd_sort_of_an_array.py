# @l2g 1998 python3
# [1998] GCD Sort of an Array
# Difficulty: Hard
# https://leetcode.com/problems/gcd-sort-of-an-array
#
# You are given an integer array nums,
# and you can perform the following operation any number of times on nums:
#
# Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i],
# nums[j]) > 1 where gcd(nums[i],nums[j]) is the greatest common divisor of nums[i] and nums[j].
#
# Return true if it is possible to sort nums in non-decreasing order using the above swap method,
# or false otherwise.
#
# Example 1:
#
# Input: nums = [7,21,3]
# Output: true
# Explanation: We can sort [7,21,3] by performing the following operations:
# - Swap 7 and 21 because gcd(7,21) = 7. nums = [21,7,3]
# - Swap 21 and 3 because gcd(21,3) = 3. nums = [3,7,21]
#
# Example 2:
#
# Input: nums = [5,2,6,2]
# Output: false
# Explanation: It is impossible to sort the array because 5 cannot be swapped with any other element.
#
# Example 3:
#
# Input: nums = [10,5,9,3,15]
# Output: true
# We can sort [10,5,9,3,15] by performing the following operations:
# - Swap 10 and 15 because gcd(10,15) = 5. nums = [15,5,9,3,10]
# - Swap 15 and 3 because gcd(15,3) = 3. nums = [3,5,9,15,10]
# - Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,10,15]
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# 2 <= nums[i] <= 10^5
#
#

from typing import List


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        class DSU:
            def __init__(self, n):
                self._data = list(range(n))

            def find(self, a):
                if self._data[a] != a:
                    self._data[a] = self.find(self._data[a])
                return self._data[a]

            def union(self, a, b):
                a, b = self.find(a), self.find(b)

                if a != b:
                    self._data[b] = a

        num_set = [i for i in range(10 ** 5 + 1)]
        for i in range(2, 10 ** 5 + 1):
            if num_set[i] == i:
                pos = i * i
                while pos < len(num_set):
                    num_set[pos] = min(num_set[pos], i)
                    pos += i

        dsu = DSU(max(nums) + 1)
        # union nums
        for i, num in enumerate(nums):
            val = num
            while val > 1:
                min_num = num_set[val]
                dsu.union(min_num, num)
                val //= min_num

        sorted_num = sorted(nums)
        for i in range(len(nums)):
            if dsu.find(sorted_num[i]) != dsu.find(nums[i]):
                return False

        return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1998.py")])
