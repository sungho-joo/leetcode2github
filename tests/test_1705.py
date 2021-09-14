#!/usr/bin/env python

import pytest

"""
Test 1705. Maximum Number of Eaten Apples
"""


@pytest.fixture(scope="session")
def init_variables_1705():
    from src.leetcode_1705_maximum_number_of_eaten_apples import Solution

    solution = Solution()

    def _init_variables_1705():
        return solution

    yield _init_variables_1705


class TestClass1705:
    def test_solution_0(self, init_variables_1705):
        assert init_variables_1705().eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]) == 7

    def test_solution_1(self, init_variables_1705):
        assert init_variables_1705().eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]) == 5
