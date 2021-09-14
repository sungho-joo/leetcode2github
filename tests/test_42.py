#!/usr/bin/env python

import pytest

"""
Test 42. Trapping Rain Water
"""


@pytest.fixture(scope="session")
def init_variables_42():
    from src.leetcode_42_trapping_rain_water import Solution

    solution = Solution()

    def _init_variables_42():
        return solution

    yield _init_variables_42


class TestClass42:
    def test_solution_0(self, init_variables_42):
        assert init_variables_42().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_solution_1(self, init_variables_42):
        assert init_variables_42().trap([4, 2, 0, 3, 2, 5]) == 9


#!/usr/bin/env python

import pytest

"""
Test 42. Trapping Rain Water
"""


@pytest.fixture(scope="session")
def init_variables_42():
    from src.leetcode_42_trapping_rain_water import Solution

    solution = Solution()

    def _init_variables_42():
        return solution

    yield _init_variables_42


class TestClass42:
    def test_solution_0(self, init_variables_42):
        assert init_variables_42().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_solution_1(self, init_variables_42):
        assert init_variables_42().trap([4, 2, 0, 3, 2, 5]) == 9
