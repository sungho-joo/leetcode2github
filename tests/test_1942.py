#!/usr/bin/env python

import pytest

"""
Test 1942. The Number of the Smallest Unoccupied Chair
"""


@pytest.fixture(scope="session")
def init_variables_1942():
    from src.leetcode_1942_the_number_of_the_smallest_unoccupied_chair import Solution

    solution = Solution()

    def _init_variables_1942():
        return solution

    yield _init_variables_1942


class TestClass1942:
    def test_solution_0(self, init_variables_1942):
        assert init_variables_1942().smallestChair([[1, 4], [2, 3], [4, 6]], 1) == 1

    def test_solution_1(self, init_variables_1942):
        assert init_variables_1942().smallestChair([[3, 10], [1, 5], [2, 6]], 0) == 2


#!/usr/bin/env python

import pytest

"""
Test 1942. The Number of the Smallest Unoccupied Chair
"""


@pytest.fixture(scope="session")
def init_variables_1942():
    from src.leetcode_1942_the_number_of_the_smallest_unoccupied_chair import Solution

    solution = Solution()

    def _init_variables_1942():
        return solution

    yield _init_variables_1942


class TestClass1942:
    def test_solution_0(self, init_variables_1942):
        assert init_variables_1942().smallestChair([[1, 4], [2, 3], [4, 6]], 1) == 1

    def test_solution_1(self, init_variables_1942):
        assert init_variables_1942().smallestChair([[3, 10], [1, 5], [2, 6]], 0) == 2
