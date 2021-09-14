#!/usr/bin/env python

import pytest

"""
Test 932. Beautiful Array
"""


@pytest.fixture(scope="session")
def init_variables_932():
    from src.leetcode_932_beautiful_array import Solution

    solution = Solution()

    def _init_variables_932():
        return solution

    yield _init_variables_932


class TestClass932:
    def test_solution_0(self, init_variables_932):
        assert init_variables_932().beautifulArray(4) == [2, 1, 4, 3]

    def test_solution_1(self, init_variables_932):
        assert init_variables_932().beautifulArray(5) == [3, 1, 2, 5, 4]


#!/usr/bin/env python

import pytest

"""
Test 932. Beautiful Array
"""


@pytest.fixture(scope="session")
def init_variables_932():
    from src.leetcode_932_beautiful_array import Solution

    solution = Solution()

    def _init_variables_932():
        return solution

    yield _init_variables_932


class TestClass932:
    def test_solution_0(self, init_variables_932):
        assert init_variables_932().beautifulArray(4) == [2, 1, 4, 3]

    def test_solution_1(self, init_variables_932):
        assert init_variables_932().beautifulArray(5) == [3, 1, 2, 5, 4]
