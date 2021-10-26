#!/usr/bin/env python

import pytest

"""
Test 374. Guess Number Higher or Lower
"""


@pytest.fixture(scope="session")
def init_variables_374():
    from src.leetcode_374_guess_number_higher_or_lower import Solution

    solution = Solution()

    def _init_variables_374():
        return solution

    yield _init_variables_374


class TestClass374:
    def test_solution_0(self, init_variables_374):
        assert init_variables_374().guessNumber(10, 6) == 6

    def test_solution_1(self, init_variables_374):
        assert init_variables_374().guessNumber(1, 1) == 1

    def test_solution_2(self, init_variables_374):
        assert init_variables_374().guessNumber(2, 1) == 1

    def test_solution_3(self, init_variables_374):
        assert init_variables_374().guessNumber(2, 2) == 2
