#!/usr/bin/env python

import pytest

"""
Test 1849. Splitting a String Into Descending Consecutive Values
"""


@pytest.fixture(scope="session")
def init_variables_1849():
    from src.leetcode_1849_splitting_a_string_into_descending_consecutive_values import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1849():
        return solution

    yield _init_variables_1849


class TestClass1849:
    def test_solution_0(self, init_variables_1849):
        assert not init_variables_1849().splitString("1234")

    def test_solution_1(self, init_variables_1849):
        assert init_variables_1849().splitString("050043")

    def test_solution_2(self, init_variables_1849):
        assert not init_variables_1849().splitString("9080701")

    def test_solution_3(self, init_variables_1849):
        assert init_variables_1849().splitString("10009998")


#!/usr/bin/env python

import pytest

"""
Test 1849. Splitting a String Into Descending Consecutive Values
"""


@pytest.fixture(scope="session")
def init_variables_1849():
    from src.leetcode_1849_splitting_a_string_into_descending_consecutive_values import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1849():
        return solution

    yield _init_variables_1849


class TestClass1849:
    def test_solution_0(self, init_variables_1849):
        assert not init_variables_1849().splitString("1234")

    def test_solution_1(self, init_variables_1849):
        assert init_variables_1849().splitString("050043")

    def test_solution_2(self, init_variables_1849):
        assert not init_variables_1849().splitString("9080701")

    def test_solution_3(self, init_variables_1849):
        assert init_variables_1849().splitString("10009998")
