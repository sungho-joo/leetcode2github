#!/usr/bin/env python

import pytest

"""
Test 1915. Number of Wonderful Substrings
"""


@pytest.fixture(scope="session")
def init_variables_1915():
    from src.leetcode_1915_number_of_wonderful_substrings import Solution

    solution = Solution()

    def _init_variables_1915():
        return solution

    yield _init_variables_1915


class TestClass1915:
    def test_solution_0(self, init_variables_1915):
        assert init_variables_1915().wonderfulSubstrings("aba") == 4

    def test_solution_1(self, init_variables_1915):
        assert init_variables_1915().wonderfulSubstrings("aabb") == 9

    def test_solution_2(self, init_variables_1915):
        assert init_variables_1915().wonderfulSubstrings("he") == 2


#!/usr/bin/env python

import pytest

"""
Test 1915. Number of Wonderful Substrings
"""


@pytest.fixture(scope="session")
def init_variables_1915():
    from src.leetcode_1915_number_of_wonderful_substrings import Solution

    solution = Solution()

    def _init_variables_1915():
        return solution

    yield _init_variables_1915


class TestClass1915:
    def test_solution_0(self, init_variables_1915):
        assert init_variables_1915().wonderfulSubstrings("aba") == 4

    def test_solution_1(self, init_variables_1915):
        assert init_variables_1915().wonderfulSubstrings("aabb") == 9

    def test_solution_2(self, init_variables_1915):
        assert init_variables_1915().wonderfulSubstrings("he") == 2
