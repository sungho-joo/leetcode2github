#!/usr/bin/env python

import pytest

"""
Test 1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number
"""


@pytest.fixture(scope="session")
def init_variables_1850():
    from src.leetcode_1850_minimum_adjacent_swaps_to_reach_the_kth_smallest_number import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1850():
        return solution

    yield _init_variables_1850


class TestClass1850:
    def test_solution_0(self, init_variables_1850):
        assert init_variables_1850().getMinSwaps("5489355142", 4) == 2

    def test_solution_1(self, init_variables_1850):
        assert init_variables_1850().getMinSwaps("11112", 4) == 4

    def test_solution_2(self, init_variables_1850):
        assert init_variables_1850().getMinSwaps("00123", 1) == 1


#!/usr/bin/env python

import pytest

"""
Test 1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number
"""


@pytest.fixture(scope="session")
def init_variables_1850():
    from src.leetcode_1850_minimum_adjacent_swaps_to_reach_the_kth_smallest_number import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1850():
        return solution

    yield _init_variables_1850


class TestClass1850:
    def test_solution_0(self, init_variables_1850):
        assert init_variables_1850().getMinSwaps("5489355142", 4) == 2

    def test_solution_1(self, init_variables_1850):
        assert init_variables_1850().getMinSwaps("11112", 4) == 4

    def test_solution_2(self, init_variables_1850):
        assert init_variables_1850().getMinSwaps("00123", 1) == 1
