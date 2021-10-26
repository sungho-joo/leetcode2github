#!/usr/bin/env python

import pytest

"""
Test 2023. Number of Pairs of Strings With Concatenation Equal to Target
"""


@pytest.fixture(scope="session")
def init_variables_2023():
    from src.leetcode_2023_number_of_pairs_of_strings_with_concatenation_equal_to_target import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2023():
        return solution

    yield _init_variables_2023


class TestClass2023:
    def test_solution_0(self, init_variables_2023):
        assert init_variables_2023().numOfPairs(["777", "7", "77", "77"], "7777") == 4

    def test_solution_1(self, init_variables_2023):
        assert init_variables_2023().numOfPairs(["123", "4", "12", "34"], "1234") == 2

    def test_solution_2(self, init_variables_2023):
        assert init_variables_2023().numOfPairs(["1", "1", "1"], "11") == 6
