#!/usr/bin/env python

import pytest

"""
Test 1903. Largest Odd Number in String
"""


@pytest.fixture(scope="session")
def init_variables_1903():
    from src.leetcode_1903_largest_odd_number_in_string import Solution

    solution = Solution()

    def _init_variables_1903():
        return solution

    yield _init_variables_1903


class TestClass1903:
    def test_solution_0(self, init_variables_1903):
        assert init_variables_1903().largestOddNumber("52") == "5"

    def test_solution_1(self, init_variables_1903):
        assert init_variables_1903().largestOddNumber("4206") == ""

    def test_solution_2(self, init_variables_1903):
        assert init_variables_1903().largestOddNumber("35427") == "35427"


#!/usr/bin/env python

import pytest

"""
Test 1903. Largest Odd Number in String
"""


@pytest.fixture(scope="session")
def init_variables_1903():
    from src.leetcode_1903_largest_odd_number_in_string import Solution

    solution = Solution()

    def _init_variables_1903():
        return solution

    yield _init_variables_1903


class TestClass1903:
    def test_solution_0(self, init_variables_1903):
        assert init_variables_1903().largestOddNumber("52") == "5"

    def test_solution_1(self, init_variables_1903):
        assert init_variables_1903().largestOddNumber("4206") == ""

    def test_solution_2(self, init_variables_1903):
        assert init_variables_1903().largestOddNumber("35427") == "35427"
