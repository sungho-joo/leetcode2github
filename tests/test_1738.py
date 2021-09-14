#!/usr/bin/env python

import pytest

"""
Test 1738. Find Kth Largest XOR Coordinate Value
"""


@pytest.fixture(scope="session")
def init_variables_1738():
    from src.leetcode_1738_find_kth_largest_xor_coordinate_value import Solution

    solution = Solution()

    def _init_variables_1738():
        return solution

    yield _init_variables_1738


class TestClass1738:
    def test_solution_0(self, init_variables_1738):
        assert init_variables_1738().kthLargestValue([[5, 2], [1, 6]], 1) == 7

    def test_solution_1(self, init_variables_1738):
        assert init_variables_1738().kthLargestValue([[5, 2], [1, 6]], 2) == 5

    def test_solution_2(self, init_variables_1738):
        assert init_variables_1738().kthLargestValue([[5, 2], [1, 6]], 3) == 4

    def test_solution_3(self, init_variables_1738):
        assert init_variables_1738().kthLargestValue([[5, 2], [1, 6]], 4) == 0
