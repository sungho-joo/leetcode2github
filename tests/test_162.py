#!/usr/bin/env python

import pytest

"""
Test 162. Find Peak Element
"""


@pytest.fixture(scope="session")
def init_variables_162():
    from src.leetcode_162_find_peak_element import Solution

    solution = Solution()

    def _init_variables_162():
        return solution

    yield _init_variables_162


class TestClass162:
    def test_solution_0(self, init_variables_162):
        assert init_variables_162().findPeakElement([1, 2, 3, 1]) == 2

    def test_solution_1(self, init_variables_162):
        assert init_variables_162().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5


#!/usr/bin/env python

import pytest

"""
Test 162. Find Peak Element
"""


@pytest.fixture(scope="session")
def init_variables_162():
    from src.leetcode_162_find_peak_element import Solution

    solution = Solution()

    def _init_variables_162():
        return solution

    yield _init_variables_162


class TestClass162:
    def test_solution_0(self, init_variables_162):
        assert init_variables_162().findPeakElement([1, 2, 3, 1]) == 2

    def test_solution_1(self, init_variables_162):
        assert init_variables_162().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
