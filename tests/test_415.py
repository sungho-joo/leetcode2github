#!/usr/bin/env python

import pytest

"""
Test 415. Add Strings
"""


@pytest.fixture(scope="session")
def init_variables_415():
    from src.leetcode_415_add_strings import Solution

    solution = Solution()

    def _init_variables_415():
        return solution

    yield _init_variables_415


class TestClass415:
    def test_solution_0(self, init_variables_415):
        assert init_variables_415().addStrings("11", "123") == "134"

    def test_solution_1(self, init_variables_415):
        assert init_variables_415().addStrings("456", "77") == "533"

    def test_solution_2(self, init_variables_415):
        assert init_variables_415().addStrings("0", "0") == "0"


#!/usr/bin/env python

import pytest

"""
Test 415. Add Strings
"""


@pytest.fixture(scope="session")
def init_variables_415():
    from src.leetcode_415_add_strings import Solution

    solution = Solution()

    def _init_variables_415():
        return solution

    yield _init_variables_415


class TestClass415:
    def test_solution_0(self, init_variables_415):
        assert init_variables_415().addStrings("11", "123") == "134"

    def test_solution_1(self, init_variables_415):
        assert init_variables_415().addStrings("456", "77") == "533"

    def test_solution_2(self, init_variables_415):
        assert init_variables_415().addStrings("0", "0") == "0"
