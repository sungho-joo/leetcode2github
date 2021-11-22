# @l2g 2081 python3
# [2081] Sum of k-Mirror Numbers
# Difficulty: Hard
# https://leetcode.com/problems/sum-of-k-mirror-numbers
#
# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.
#
# For example,9 is a 2-mirror number.
# The representation of 9 in base-10 and base-2 are 9 and 1001 respectively,
# which read the same both forward and backward.
# On the contrary,4 is not a 2-mirror number.The representation of 4 in base-2 is 100,
# which does not read the same both forward and backward.
#
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
#
# Example 1:
#
# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25.
#
# Example 2:
#
# Input: k = 3, n = 7
# Output: 499
# Explanation:
# The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#   base-10    base-3
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
#
# Example 3:
#
# Input: k = 7, n = 17
# Output: 20379000
# Explanation: The 17 smallest 7-mirror numbers are:
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
#
#
# Constraints:
#
# 2 <= k <= 9
# 1 <= n <= 30
#
#


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        valid_k_nums = defaultdict(list)
        valid_k_nums[0].append([])
        valid_k_nums[1] = [[str(i)] for i in range(k)]

        def check_in_dec(num_in_dec):
            num_in_dec = str(num_in_dec)
            return num_in_dec == num_in_dec[::-1]

        def get_next_num(length):
            for i in range(1, k):
                for num_list in valid_k_nums[length - 2]:
                    candi = [str(i)] + num_list + [str(i)]
                    num_in_dec = int("".join(candi), k)
                    yield num_in_dec

        if n < len(valid_k_nums[1]):
            return sum(range(1, n + 1))

        ans = sum(range(1, k))
        n -= len(valid_k_nums[1]) - 1
        length = 2
        while n > 0:
            for i in range(k):
                for num_list in valid_k_nums[length - 2]:
                    valid_k_nums[length].append([str(i)] + num_list + [str(i)])

            for next_candi in get_next_num(length):
                if check_in_dec(next_candi):
                    ans += next_candi
                    n -= 1
                    if n == 0:
                        return ans
            length += 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2081.py")])
