#!/usr/bin/env python

import pytest

"""
Test 326. Power of Three
"""


@pytest.fixture(scope="session")
def init_variables_326():
    from src.leetcode_326_power_of_three import Solution

    solution = Solution()

    def _init_variables_326():
        return solution

    yield _init_variables_326


class TestClass326:
    def test_solution_0(self, init_variables_326):
        assert init_variables_326().isPowerOfThree(27)

    def test_solution_1(self, init_variables_326):
        assert not init_variables_326().isPowerOfThree(0)

    def test_solution_2(self, init_variables_326):
        assert init_variables_326().isPowerOfThree(9)

    def test_solution_3(self, init_variables_326):
        assert not init_variables_326().isPowerOfThree(45)
