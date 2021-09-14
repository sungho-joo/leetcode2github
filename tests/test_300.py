#!/usr/bin/env python

import pytest

"""
Test 300. Longest Increasing Subsequence
"""


@pytest.fixture(scope="session")
def init_variables_300():
    from src.leetcode_300_longest_increasing_subsequence import Solution

    solution = Solution()

    def _init_variables_300():
        return solution

    yield _init_variables_300


class TestClass300:
    def test_solution_0(self, init_variables_300):
        assert init_variables_300().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_solution_1(self, init_variables_300):
        assert init_variables_300().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4

    def test_solution_2(self, init_variables_300):
        assert init_variables_300().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1


#!/usr/bin/env python

import pytest

"""
Test 300. Longest Increasing Subsequence
"""


@pytest.fixture(scope="session")
def init_variables_300():
    from src.leetcode_300_longest_increasing_subsequence import Solution

    solution = Solution()

    def _init_variables_300():
        return solution

    yield _init_variables_300


class TestClass300:
    def test_solution_0(self, init_variables_300):
        assert init_variables_300().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_solution_1(self, init_variables_300):
        assert init_variables_300().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4

    def test_solution_2(self, init_variables_300):
        assert init_variables_300().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
