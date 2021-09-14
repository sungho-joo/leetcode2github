#!/usr/bin/env python

import pytest

"""
Test 28. Implement strStr()
"""


@pytest.fixture(scope="session")
def init_variables_28():
    from src.leetcode_28_implement_strstr import Solution

    solution = Solution()

    def _init_variables_28():
        return solution

    yield _init_variables_28


class TestClass28:
    def test_solution_0(self, init_variables_28):
        assert init_variables_28().strStr("hello", "ll") == 2

    def test_solution_1(self, init_variables_28):
        assert init_variables_28().strStr("aaaaa", "bba") == -1

    def test_solution_2(self, init_variables_28):
        assert init_variables_28().strStr("", "") == 0
