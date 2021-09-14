#!/usr/bin/env python

import pytest

"""
Test 189. Rotate Array
"""


@pytest.fixture(scope="session")
def init_variables_189():
    from src.leetcode_189_rotate_array import Solution

    solution = Solution()

    def _init_variables_189():
        return solution

    yield _init_variables_189


class TestClass189:
    def test_solution_0(self, init_variables_189):
        assert init_variables_189().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

    def test_solution_1(self, init_variables_189):
        assert init_variables_189().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]


#!/usr/bin/env python

import pytest

"""
Test 189. Rotate Array
"""


@pytest.fixture(scope="session")
def init_variables_189():
    from src.leetcode_189_rotate_array import Solution

    solution = Solution()

    def _init_variables_189():
        return solution

    yield _init_variables_189


class TestClass189:
    def test_solution_0(self, init_variables_189):
        assert init_variables_189().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

    def test_solution_1(self, init_variables_189):
        assert init_variables_189().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
