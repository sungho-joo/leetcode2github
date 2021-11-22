#!/usr/bin/env python

import pytest

"""
Test 1178. Number of Valid Words for Each Puzzle
"""


@pytest.fixture(scope="session")
def init_variables_1178():
    from src.leetcode_1178_number_of_valid_words_for_each_puzzle import Solution

    solution = Solution()

    def _init_variables_1178():
        return solution

    yield _init_variables_1178


class TestClass1178:
    def test_solution_0(self, init_variables_1178):
        assert (
            init_variables_1178().findNumOfValidWords(
                ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"],
            )
            == [1, 1, 3, 2, 4, 0]
        )

    def test_solution_1(self, init_variables_1178):
        assert init_variables_1178().findNumOfValidWords(
            ["apple", "pleas", "please"], ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]
        ) == [0, 1, 3, 2, 0]
