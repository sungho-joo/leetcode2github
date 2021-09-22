#!/usr/bin/env python

import pytest

"""
Test 2. Add Two Numbers
"""


@pytest.fixture(scope="session")
def init_variables_2():
    from src.leetcode_2_add_two_numbers import Solution

    solution = Solution()

    def _init_variables_2():
        return solution

    yield _init_variables_2


class TestClass2:
    def test_solution_0(self, init_variables_2):
        assert init_variables_2().addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]

    def test_solution_1(self, init_variables_2):
        assert init_variables_2().addTwoNumbers([0], [0]) == [0]

    def test_solution_2(self, init_variables_2):
        assert init_variables_2().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [
            8,
            9,
            9,
            9,
            0,
            0,
            0,
            1,
        ]
