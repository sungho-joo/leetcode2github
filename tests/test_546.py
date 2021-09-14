#!/usr/bin/env python

import pytest

"""
Test 546. Remove Boxes
"""


@pytest.fixture(scope="session")
def init_variables_546():
    from src.leetcode_546_remove_boxes import Solution

    solution = Solution()

    def _init_variables_546():
        return solution

    yield _init_variables_546


class TestClass546:
    def test_solution_0(self, init_variables_546):
        assert init_variables_546().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23

    def test_solution_1(self, init_variables_546):
        assert init_variables_546().removeBoxes([1, 1, 1]) == 9

    def test_solution_2(self, init_variables_546):
        assert init_variables_546().removeBoxes([1]) == 1


#!/usr/bin/env python

import pytest

"""
Test 546. Remove Boxes
"""


@pytest.fixture(scope="session")
def init_variables_546():
    from src.leetcode_546_remove_boxes import Solution

    solution = Solution()

    def _init_variables_546():
        return solution

    yield _init_variables_546


class TestClass546:
    def test_solution_0(self, init_variables_546):
        assert init_variables_546().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23

    def test_solution_1(self, init_variables_546):
        assert init_variables_546().removeBoxes([1, 1, 1]) == 9

    def test_solution_2(self, init_variables_546):
        assert init_variables_546().removeBoxes([1]) == 1
