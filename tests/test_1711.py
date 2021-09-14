#!/usr/bin/env python

import pytest

"""
Test 1711. Count Good Meals
"""


@pytest.fixture(scope="session")
def init_variables_1711():
    from src.leetcode_1711_count_good_meals import Solution
    solution = Solution()

    def _init_variables_1711():
        return solution

    yield _init_variables_1711

class TestClass1711:
    def test_solution_0(self, init_variables_1711):
        assert init_variables_1711().                            countPairs([1,3,5,7,9]) == 4

    def test_solution_1(self, init_variables_1711):
        assert init_variables_1711().                            countPairs([1,1,1,3,3,3,7]) == 15
