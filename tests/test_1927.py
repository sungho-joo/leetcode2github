#!/usr/bin/env python

import pytest

"""
Test 1927. Sum Game
"""


@pytest.fixture(scope="session")
def init_variables_1927():
    from src.leetcode_1927_sum_game import Solution

    solution = Solution()

    def _init_variables_1927():
        return solution

    yield _init_variables_1927


class TestClass1927:
    def test_solution_0(self, init_variables_1927):
        assert not init_variables_1927().sumGame("5023")

    def test_solution_1(self, init_variables_1927):
        assert init_variables_1927().sumGame("25??")

    def test_solution_2(self, init_variables_1927):
        assert not init_variables_1927().sumGame("?3295???")


#!/usr/bin/env python

import pytest

"""
Test 1927. Sum Game
"""


@pytest.fixture(scope="session")
def init_variables_1927():
    from src.leetcode_1927_sum_game import Solution

    solution = Solution()

    def _init_variables_1927():
        return solution

    yield _init_variables_1927


class TestClass1927:
    def test_solution_0(self, init_variables_1927):
        assert not init_variables_1927().sumGame("5023")

    def test_solution_1(self, init_variables_1927):
        assert init_variables_1927().sumGame("25??")

    def test_solution_2(self, init_variables_1927):
        assert not init_variables_1927().sumGame("?3295???")
