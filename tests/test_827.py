#!/usr/bin/env python

import pytest

"""
Test 827. Making A Large Island
"""


@pytest.fixture(scope="session")
def init_variables_827():
    from src.leetcode_827_making_a_large_island import Solution

    solution = Solution()

    def _init_variables_827():
        return solution

    yield _init_variables_827


class TestClass827:
    def test_solution_0(self, init_variables_827):
        assert init_variables_827().largestIsland([[1, 0], [0, 1]]) == 3

    def test_solution_1(self, init_variables_827):
        assert init_variables_827().largestIsland([[1, 1], [1, 0]]) == 4

    def test_solution_2(self, init_variables_827):
        assert init_variables_827().largestIsland([[1, 1], [1, 1]]) == 4


#!/usr/bin/env python

import pytest

"""
Test 827. Making A Large Island
"""


@pytest.fixture(scope="session")
def init_variables_827():
    from src.leetcode_827_making_a_large_island import Solution

    solution = Solution()

    def _init_variables_827():
        return solution

    yield _init_variables_827


class TestClass827:
    def test_solution_0(self, init_variables_827):
        assert init_variables_827().largestIsland([[1, 0], [0, 1]]) == 3

    def test_solution_1(self, init_variables_827):
        assert init_variables_827().largestIsland([[1, 1], [1, 0]]) == 4

    def test_solution_2(self, init_variables_827):
        assert init_variables_827().largestIsland([[1, 1], [1, 1]]) == 4
