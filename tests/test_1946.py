#!/usr/bin/env python

import pytest

"""
Test 1946. Largest Number After Mutating Substring
"""


@pytest.fixture(scope="session")
def init_variables_1946():
    from src.leetcode_1946_largest_number_after_mutating_substring import Solution

    solution = Solution()

    def _init_variables_1946():
        return solution

    yield _init_variables_1946


class TestClass1946:
    def test_solution_0(self, init_variables_1946):
        assert init_variables_1946().maximumNumber("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832"

    def test_solution_1(self, init_variables_1946):
        assert init_variables_1946().maximumNumber("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == "934"

    def test_solution_2(self, init_variables_1946):
        assert init_variables_1946().maximumNumber("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == "5"


#!/usr/bin/env python

import pytest

"""
Test 1946. Largest Number After Mutating Substring
"""


@pytest.fixture(scope="session")
def init_variables_1946():
    from src.leetcode_1946_largest_number_after_mutating_substring import Solution

    solution = Solution()

    def _init_variables_1946():
        return solution

    yield _init_variables_1946


class TestClass1946:
    def test_solution_0(self, init_variables_1946):
        assert init_variables_1946().maximumNumber("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832"

    def test_solution_1(self, init_variables_1946):
        assert init_variables_1946().maximumNumber("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == "934"

    def test_solution_2(self, init_variables_1946):
        assert init_variables_1946().maximumNumber("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == "5"
