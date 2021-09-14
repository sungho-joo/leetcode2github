#!/usr/bin/env python

import pytest

"""
Test 1967. Number of Strings That Appear as Substrings in Word
"""


@pytest.fixture(scope="session")
def init_variables_1967():
    from src.leetcode_1967_number_of_strings_that_appear_as_substrings_in_word import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1967():
        return solution

    yield _init_variables_1967


class TestClass1967:
    def test_solution_0(self, init_variables_1967):
        assert init_variables_1967().numOfStrings(["a", "abc", "bc", "d"], "abc") == 3

    def test_solution_1(self, init_variables_1967):
        assert init_variables_1967().numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2

    def test_solution_2(self, init_variables_1967):
        assert init_variables_1967().numOfStrings(["a", "a", "a"], "ab") == 3
