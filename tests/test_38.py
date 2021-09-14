#!/usr/bin/env python

import pytest

"""
Test 38. Count and Say
"""


@pytest.fixture(scope="session")
def init_variables_38():
    from src.leetcode_38_count_and_say import Solution

    solution = Solution()

    def _init_variables_38():
        return solution

    yield _init_variables_38


class TestClass38:
    def test_solution_0(self, init_variables_38):
        assert init_variables_38().countAndSay(1) == "1"

    def test_solution_1(self, init_variables_38):
        assert init_variables_38().countAndSay(4) == "1211"
