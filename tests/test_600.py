#!/usr/bin/env python

import pytest

"""
Test 600. Non-negative Integers without Consecutive Ones
"""


@pytest.fixture(scope="session")
def init_variables_600():
    from src.leetcode_600_non_negative_integers_without_consecutive_ones import Solution

    solution = Solution()

    def _init_variables_600():
        return solution

    yield _init_variables_600


class TestClass600:
    def test_solution_0(self, init_variables_600):
        assert init_variables_600().findIntegers(5) == 5

    def test_solution_1(self, init_variables_600):
        assert init_variables_600().findIntegers(1) == 2

    def test_solution_2(self, init_variables_600):
        assert init_variables_600().findIntegers(2) == 3


#!/usr/bin/env python

import pytest

"""
Test 600. Non-negative Integers without Consecutive Ones
"""


@pytest.fixture(scope="session")
def init_variables_600():
    from src.leetcode_600_non_negative_integers_without_consecutive_ones import Solution

    solution = Solution()

    def _init_variables_600():
        return solution

    yield _init_variables_600


class TestClass600:
    def test_solution_0(self, init_variables_600):
        assert init_variables_600().findIntegers(5) == 5

    def test_solution_1(self, init_variables_600):
        assert init_variables_600().findIntegers(1) == 2

    def test_solution_2(self, init_variables_600):
        assert init_variables_600().findIntegers(2) == 3
