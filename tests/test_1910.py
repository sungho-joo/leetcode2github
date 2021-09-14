#!/usr/bin/env python

import pytest

"""
Test 1910. Remove All Occurrences of a Substring
"""


@pytest.fixture(scope="session")
def init_variables_1910():
    from src.leetcode_1910_remove_all_occurrences_of_a_substring import Solution

    solution = Solution()

    def _init_variables_1910():
        return solution

    yield _init_variables_1910


class TestClass1910:
    def test_solution_0(self, init_variables_1910):
        assert init_variables_1910().removeOccurrences("daabcbaabcbc", "abc") == "dab"

    def test_solution_1(self, init_variables_1910):
        assert init_variables_1910().removeOccurrences("axxxxyyyyb", "xy") == "ab"


#!/usr/bin/env python

import pytest

"""
Test 1910. Remove All Occurrences of a Substring
"""


@pytest.fixture(scope="session")
def init_variables_1910():
    from src.leetcode_1910_remove_all_occurrences_of_a_substring import Solution

    solution = Solution()

    def _init_variables_1910():
        return solution

    yield _init_variables_1910


class TestClass1910:
    def test_solution_0(self, init_variables_1910):
        assert init_variables_1910().removeOccurrences("daabcbaabcbc", "abc") == "dab"

    def test_solution_1(self, init_variables_1910):
        assert init_variables_1910().removeOccurrences("axxxxyyyyb", "xy") == "ab"
