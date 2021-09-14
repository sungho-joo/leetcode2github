#!/usr/bin/env python

import pytest

"""
Test 76. Minimum Window Substring
"""


@pytest.fixture(scope="session")
def init_variables_76():
    from src.leetcode_76_minimum_window_substring import Solution

    solution = Solution()

    def _init_variables_76():
        return solution

    yield _init_variables_76


class TestClass76:
    def test_solution_0(self, init_variables_76):
        assert init_variables_76().minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_solution_1(self, init_variables_76):
        assert init_variables_76().minWindow("a", "a") == "a"

    def test_solution_2(self, init_variables_76):
        assert init_variables_76().minWindow("a", "aa") == ""


#!/usr/bin/env python

import pytest

"""
Test 76. Minimum Window Substring
"""


@pytest.fixture(scope="session")
def init_variables_76():
    from src.leetcode_76_minimum_window_substring import Solution

    solution = Solution()

    def _init_variables_76():
        return solution

    yield _init_variables_76


class TestClass76:
    def test_solution_0(self, init_variables_76):
        assert init_variables_76().minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_solution_1(self, init_variables_76):
        assert init_variables_76().minWindow("a", "a") == "a"

    def test_solution_2(self, init_variables_76):
        assert init_variables_76().minWindow("a", "aa") == ""
