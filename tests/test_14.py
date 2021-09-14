#!/usr/bin/env python

import pytest

"""
Test 14. Longest Common Prefix
"""


@pytest.fixture(scope="session")
def init_variables_14():
    from src.leetcode_14_longest_common_prefix import Solution

    solution = Solution()

    def _init_variables_14():
        return solution

    yield _init_variables_14


class TestClass14:
    def test_solution_0(self, init_variables_14):
        assert init_variables_14().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    def test_solution_1(self, init_variables_14):
        assert init_variables_14().longestCommonPrefix(["dog", "racecar", "car"]) == ""
