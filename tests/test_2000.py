#!/usr/bin/env python

import pytest

"""
Test 2000. Reverse Prefix of Word
"""


@pytest.fixture(scope="session")
def init_variables_2000():
    from src.leetcode_2000_reverse_prefix_of_word import Solution

    solution = Solution()

    def _init_variables_2000():
        return solution

    yield _init_variables_2000


class TestClass2000:
    def test_solution_0(self, init_variables_2000):
        assert init_variables_2000().reversePrefix("abcdefd", "d") == "dcbaefd"

    def test_solution_1(self, init_variables_2000):
        assert init_variables_2000().reversePrefix("xyxzxe", "z") == "zxyxxe"

    def test_solution_2(self, init_variables_2000):
        assert init_variables_2000().reversePrefix("abcd", "z") == "abcd"
