#!/usr/bin/env python

import pytest

"""
Test 424. Longest Repeating Character Replacement
"""


@pytest.fixture(scope="session")
def init_variables_424():
    from src.leetcode_424_longest_repeating_character_replacement import Solution

    solution = Solution()

    def _init_variables_424():
        return solution

    yield _init_variables_424


class TestClass424:
    def test_solution_0(self, init_variables_424):
        assert init_variables_424().characterReplacement("ABAB", 2) == 4

    def test_solution_1(self, init_variables_424):
        assert init_variables_424().characterReplacement("AABABBA", 1) == 4
