#!/usr/bin/env python

import pytest

"""
Test 89. Gray Code
"""


@pytest.fixture(scope="session")
def init_variables_89():
    from src.leetcode_89_gray_code import Solution

    solution = Solution()

    def _init_variables_89():
        return solution

    yield _init_variables_89


class TestClass89:
    def test_solution_0(self, init_variables_89):
        assert init_variables_89().grayCode(2) == [0, 1, 3, 2]

    def test_solution_1(self, init_variables_89):
        assert init_variables_89().grayCode(1) == [0, 1]


#!/usr/bin/env python

import pytest

"""
Test 89. Gray Code
"""


@pytest.fixture(scope="session")
def init_variables_89():
    from src.leetcode_89_gray_code import Solution

    solution = Solution()

    def _init_variables_89():
        return solution

    yield _init_variables_89


class TestClass89:
    def test_solution_0(self, init_variables_89):
        assert init_variables_89().grayCode(2) == [0, 1, 3, 2]

    def test_solution_1(self, init_variables_89):
        assert init_variables_89().grayCode(1) == [0, 1]
