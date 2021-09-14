#!/usr/bin/env python

import pytest

"""
Test 73. Set Matrix Zeroes
"""


@pytest.fixture(scope="session")
def init_variables_73():
    from src.leetcode_73_set_matrix_zeroes import Solution

    solution = Solution()

    def _init_variables_73():
        return solution

    yield _init_variables_73


class TestClass73:
    def test_solution_0(self, init_variables_73):
        assert init_variables_73().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]

    def test_solution_1(self, init_variables_73):
        assert init_variables_73().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0],
        ]


#!/usr/bin/env python

import pytest

"""
Test 73. Set Matrix Zeroes
"""


@pytest.fixture(scope="session")
def init_variables_73():
    from src.leetcode_73_set_matrix_zeroes import Solution

    solution = Solution()

    def _init_variables_73():
        return solution

    yield _init_variables_73


class TestClass73:
    def test_solution_0(self, init_variables_73):
        assert init_variables_73().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]

    def test_solution_1(self, init_variables_73):
        assert init_variables_73().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0],
        ]
