#!/usr/bin/env python

import pytest

"""
Test 363. Max Sum of Rectangle No Larger Than K
"""


@pytest.fixture(scope="session")
def init_variables_363():
    from src.leetcode_363_max_sum_of_rectangle_no_larger_than_k import Solution

    solution = Solution()

    def _init_variables_363():
        return solution

    yield _init_variables_363


class TestClass363:
    def test_solution_0(self, init_variables_363):
        assert init_variables_363().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2) == 2

    def test_solution_1(self, init_variables_363):
        assert init_variables_363().maxSumSubmatrix([[2, 2, -1]], 3) == 3


#!/usr/bin/env python

import pytest

"""
Test 363. Max Sum of Rectangle No Larger Than K
"""


@pytest.fixture(scope="session")
def init_variables_363():
    from src.leetcode_363_max_sum_of_rectangle_no_larger_than_k import Solution

    solution = Solution()

    def _init_variables_363():
        return solution

    yield _init_variables_363


class TestClass363:
    def test_solution_0(self, init_variables_363):
        assert init_variables_363().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2) == 2

    def test_solution_1(self, init_variables_363):
        assert init_variables_363().maxSumSubmatrix([[2, 2, -1]], 3) == 3
