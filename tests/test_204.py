#!/usr/bin/env python

import pytest

"""
Test 204. Count Primes
"""


@pytest.fixture(scope="session")
def init_variables_204():
    from src.leetcode_204_count_primes import Solution

    solution = Solution()

    def _init_variables_204():
        return solution

    yield _init_variables_204


class TestClass204:
    def test_solution_0(self, init_variables_204):
        assert init_variables_204().countPrimes(10) == 4

    def test_solution_1(self, init_variables_204):
        assert init_variables_204().countPrimes(0) == 0

    def test_solution_2(self, init_variables_204):
        assert init_variables_204().countPrimes(1) == 0
