#!/usr/bin/env python

import pytest

"""
Test 17. Letter Combinations of a Phone Number
"""


@pytest.fixture(scope="session")
def init_variables_17():
    from src.leetcode_17_letter_combinations_of_a_phone_number import Solution

    solution = Solution()

    def _init_variables_17():
        return solution

    yield _init_variables_17


class TestClass17:
    def test_solution_0(self, init_variables_17):
        assert init_variables_17().letterCombinations("23") == [
            "ad",
            "ae",
            "af",
            "bd",
            "be",
            "bf",
            "cd",
            "ce",
            "cf",
        ]

    def test_solution_1(self, init_variables_17):
        assert init_variables_17().letterCombinations("") == []

    def test_solution_2(self, init_variables_17):
        assert init_variables_17().letterCombinations("2") == ["a", "b", "c"]
