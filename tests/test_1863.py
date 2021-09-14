#!/usr/bin/env python

import pytest

"""
Test 1863. Sum of All Subset XOR Totals
"""


@pytest.fixture(scope="session")
def init_variables_1863():
    from src.leetcode_1863_sum_of_all_subset_xor_totals import Solution

    solution = Solution()

    def _init_variables_1863():
        return solution

    yield _init_variables_1863


class TestClass1863:
    def test_solution_0(self, init_variables_1863):
        assert init_variables_1863().subsetXORSum([1, 3]) == 6

    def test_solution_1(self, init_variables_1863):
        assert init_variables_1863().subsetXORSum([5, 1, 6]) == 28

    def test_solution_2(self, init_variables_1863):
        assert init_variables_1863().subsetXORSum([3, 4, 5, 6, 7, 8]) == 480


#!/usr/bin/env python

import pytest

"""
Test 1863. Sum of All Subset XOR Totals
"""


@pytest.fixture(scope="session")
def init_variables_1863():
    from src.leetcode_1863_sum_of_all_subset_xor_totals import Solution

    solution = Solution()

    def _init_variables_1863():
        return solution

    yield _init_variables_1863


class TestClass1863:
    def test_solution_0(self, init_variables_1863):
        assert init_variables_1863().subsetXORSum([1, 3]) == 6

    def test_solution_1(self, init_variables_1863):
        assert init_variables_1863().subsetXORSum([5, 1, 6]) == 28

    def test_solution_2(self, init_variables_1863):
        assert init_variables_1863().subsetXORSum([3, 4, 5, 6, 7, 8]) == 480
