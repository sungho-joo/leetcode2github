#!/usr/bin/env python

import pytest

"""
Test 1954. Minimum Garden Perimeter to Collect Enough Apples
"""


@pytest.fixture(scope="session")
def init_variables_1954():
    from src.leetcode_1954_minimum_garden_perimeter_to_collect_enough_apples import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1954():
        return solution

    yield _init_variables_1954


class TestClass1954:
    def test_solution_0(self, init_variables_1954):
        assert init_variables_1954().minimumPerimeter(1) == 8

    def test_solution_1(self, init_variables_1954):
        assert init_variables_1954().minimumPerimeter(13) == 16

    def test_solution_2(self, init_variables_1954):
        assert init_variables_1954().minimumPerimeter(1000000000) == 5040


#!/usr/bin/env python

import pytest

"""
Test 1954. Minimum Garden Perimeter to Collect Enough Apples
"""


@pytest.fixture(scope="session")
def init_variables_1954():
    from src.leetcode_1954_minimum_garden_perimeter_to_collect_enough_apples import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1954():
        return solution

    yield _init_variables_1954


class TestClass1954:
    def test_solution_0(self, init_variables_1954):
        assert init_variables_1954().minimumPerimeter(1) == 8

    def test_solution_1(self, init_variables_1954):
        assert init_variables_1954().minimumPerimeter(13) == 16

    def test_solution_2(self, init_variables_1954):
        assert init_variables_1954().minimumPerimeter(1000000000) == 5040
