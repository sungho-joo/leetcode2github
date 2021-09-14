#!/usr/bin/env python

import pytest

"""
Test 1848. Minimum Distance to the Target Element
"""


@pytest.fixture(scope="session")
def init_variables_1848():
    from src.leetcode_1848_minimum_distance_to_the_target_element import Solution

    solution = Solution()

    def _init_variables_1848():
        return solution

    yield _init_variables_1848


class TestClass1848:
    def test_solution_0(self, init_variables_1848):
        assert init_variables_1848().getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1

    def test_solution_1(self, init_variables_1848):
        assert init_variables_1848().getMinDistance([1], 1, 0) == 0

    def test_solution_2(self, init_variables_1848):
        assert init_variables_1848().getMinDistance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0) == 0


#!/usr/bin/env python

import pytest

"""
Test 1848. Minimum Distance to the Target Element
"""


@pytest.fixture(scope="session")
def init_variables_1848():
    from src.leetcode_1848_minimum_distance_to_the_target_element import Solution

    solution = Solution()

    def _init_variables_1848():
        return solution

    yield _init_variables_1848


class TestClass1848:
    def test_solution_0(self, init_variables_1848):
        assert init_variables_1848().getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1

    def test_solution_1(self, init_variables_1848):
        assert init_variables_1848().getMinDistance([1], 1, 0) == 0

    def test_solution_2(self, init_variables_1848):
        assert init_variables_1848().getMinDistance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0) == 0
