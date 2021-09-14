#!/usr/bin/env python

import pytest

"""
Test 611. Valid Triangle Number
"""


@pytest.fixture(scope="session")
def init_variables_611():
    from src.leetcode_611_valid_triangle_number import Solution

    solution = Solution()

    def _init_variables_611():
        return solution

    yield _init_variables_611


class TestClass611:
    def test_solution_0(self, init_variables_611):
        assert init_variables_611().triangleNumber([2, 2, 3, 4]) == 3

    def test_solution_1(self, init_variables_611):
        assert init_variables_611().triangleNumber([4, 2, 3, 4]) == 4


#!/usr/bin/env python

import pytest

"""
Test 611. Valid Triangle Number
"""


@pytest.fixture(scope="session")
def init_variables_611():
    from src.leetcode_611_valid_triangle_number import Solution

    solution = Solution()

    def _init_variables_611():
        return solution

    yield _init_variables_611


class TestClass611:
    def test_solution_0(self, init_variables_611):
        assert init_variables_611().triangleNumber([2, 2, 3, 4]) == 3

    def test_solution_1(self, init_variables_611):
        assert init_variables_611().triangleNumber([4, 2, 3, 4]) == 4
