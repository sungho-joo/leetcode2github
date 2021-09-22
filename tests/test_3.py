#!/usr/bin/env python

import pytest

"""
Test 3. Longest Substring Without Repeating Characters
"""


@pytest.fixture(scope="session")
def init_variables_3():
    from src.leetcode_3_longest_substring_without_repeating_characters import Solution

    solution = Solution()

    def _init_variables_3():
        return solution

    yield _init_variables_3


class TestClass3:
    def test_solution_0(self, init_variables_3):
        assert init_variables_3().lengthOfLongestSubstring("abcabcbb") == 3

    def test_solution_1(self, init_variables_3):
        assert init_variables_3().lengthOfLongestSubstring("bbbbb") == 1

    def test_solution_2(self, init_variables_3):
        assert init_variables_3().lengthOfLongestSubstring("pwwkew") == 3

    def test_solution_3(self, init_variables_3):
        assert init_variables_3().lengthOfLongestSubstring("") == 0
