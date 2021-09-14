#!/usr/bin/env python

import pytest

"""
Test 378. Kth Smallest Element in a Sorted Matrix
"""


@pytest.fixture(scope="session")
def init_variables_378():
    from src.leetcode_378_kth_smallest_element_in_a_sorted_matrix import Solution

    solution = Solution()

    def _init_variables_378():
        return solution

    yield _init_variables_378


class TestClass378:
    def test_solution_0(self, init_variables_378):
        assert init_variables_378().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13

    def test_solution_1(self, init_variables_378):
        assert init_variables_378().kthSmallest([[-5]], 1) == -5


#!/usr/bin/env python

import pytest

"""
Test 378. Kth Smallest Element in a Sorted Matrix
"""


@pytest.fixture(scope="session")
def init_variables_378():
    from src.leetcode_378_kth_smallest_element_in_a_sorted_matrix import Solution

    solution = Solution()

    def _init_variables_378():
        return solution

    yield _init_variables_378


class TestClass378:
    def test_solution_0(self, init_variables_378):
        assert init_variables_378().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13

    def test_solution_1(self, init_variables_378):
        assert init_variables_378().kthSmallest([[-5]], 1) == -5
