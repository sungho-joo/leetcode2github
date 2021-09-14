#!/usr/bin/env python

import pytest

"""
Test 877. Stone Game
"""


@pytest.fixture(scope="session")
def init_variables_877():
    from src.leetcode_877_stone_game import Solution

    solution = Solution()

    def _init_variables_877():
        return solution

    yield _init_variables_877


class TestClass877:
    def test_solution_0(self, init_variables_877):
        assert init_variables_877().stoneGame([5, 3, 4, 5])

    def test_solution_1(self, init_variables_877):
        assert init_variables_877().stoneGame([3, 7, 2, 3])


#!/usr/bin/env python

import pytest

"""
Test 877. Stone Game
"""


@pytest.fixture(scope="session")
def init_variables_877():
    from src.leetcode_877_stone_game import Solution

    solution = Solution()

    def _init_variables_877():
        return solution

    yield _init_variables_877


class TestClass877:
    def test_solution_0(self, init_variables_877):
        assert init_variables_877().stoneGame([5, 3, 4, 5])

    def test_solution_1(self, init_variables_877):
        assert init_variables_877().stoneGame([3, 7, 2, 3])
