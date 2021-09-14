#!/usr/bin/env python

import pytest

"""
Test 1909. Remove One Element to Make the Array Strictly Increasing
"""


@pytest.fixture(scope="session")
def init_variables_1909():
    from src.leetcode_1909_remove_one_element_to_make_the_array_strictly_increasing import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1909():
        return solution

    yield _init_variables_1909


class TestClass1909:
    def test_solution_0(self, init_variables_1909):
        assert init_variables_1909().canBeIncreasing([1, 2, 10, 5, 7])

    def test_solution_1(self, init_variables_1909):
        assert not init_variables_1909().canBeIncreasing([2, 3, 1, 2])

    def test_solution_2(self, init_variables_1909):
        assert not init_variables_1909().canBeIncreasing([1, 1, 1])

    def test_solution_3(self, init_variables_1909):
        assert init_variables_1909().canBeIncreasing([1, 2, 3])


#!/usr/bin/env python

import pytest

"""
Test 1909. Remove One Element to Make the Array Strictly Increasing
"""


@pytest.fixture(scope="session")
def init_variables_1909():
    from src.leetcode_1909_remove_one_element_to_make_the_array_strictly_increasing import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1909():
        return solution

    yield _init_variables_1909


class TestClass1909:
    def test_solution_0(self, init_variables_1909):
        assert init_variables_1909().canBeIncreasing([1, 2, 10, 5, 7])

    def test_solution_1(self, init_variables_1909):
        assert not init_variables_1909().canBeIncreasing([2, 3, 1, 2])

    def test_solution_2(self, init_variables_1909):
        assert not init_variables_1909().canBeIncreasing([1, 1, 1])

    def test_solution_3(self, init_variables_1909):
        assert init_variables_1909().canBeIncreasing([1, 2, 3])
