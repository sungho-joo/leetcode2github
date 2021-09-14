#!/usr/bin/env python

import pytest

"""
Test 16. 3Sum Closest
"""


@pytest.fixture(scope="session")
def init_variables_16():
    from src.leetcode_16_3sum_closest import Solution

    solution = Solution()

    def _init_variables_16():
        return solution

    yield _init_variables_16


class TestClass16:
    def test_solution_0(self, init_variables_16):
        assert init_variables_16().threeSumClosest([-1, 2, 1, -4], 1) == 2

    def test_solution_1(self, init_variables_16):
        assert init_variables_16().threeSumClosest([0, 0, 0], 1) == 0


#!/usr/bin/env python

import pytest

"""
Test 16. 3Sum Closest
"""


@pytest.fixture(scope="session")
def init_variables_16():
    from src.leetcode_16_3sum_closest import Solution

    solution = Solution()

    def _init_variables_16():
        return solution

    yield _init_variables_16


class TestClass16:
    def test_solution_0(self, init_variables_16):
        assert init_variables_16().threeSumClosest([-1, 2, 1, -4], 1) == 2

    def test_solution_1(self, init_variables_16):
        assert init_variables_16().threeSumClosest([0, 0, 0], 1) == 0
