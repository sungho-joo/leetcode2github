#!/usr/bin/env python

import pytest

"""
Test 1945. Sum of Digits of String After Convert
"""


@pytest.fixture(scope="session")
def init_variables_1945():
    from src.leetcode_1945_sum_of_digits_of_string_after_convert import Solution

    solution = Solution()

    def _init_variables_1945():
        return solution

    yield _init_variables_1945


class TestClass1945:
    def test_solution_0(self, init_variables_1945):
        assert init_variables_1945().getLucky("iiii", 1) == 36

    def test_solution_1(self, init_variables_1945):
        assert init_variables_1945().getLucky("leetcode", 2) == 6

    def test_solution_2(self, init_variables_1945):
        assert init_variables_1945().getLucky("zbax", 2) == 8


#!/usr/bin/env python

import pytest

"""
Test 1945. Sum of Digits of String After Convert
"""


@pytest.fixture(scope="session")
def init_variables_1945():
    from src.leetcode_1945_sum_of_digits_of_string_after_convert import Solution

    solution = Solution()

    def _init_variables_1945():
        return solution

    yield _init_variables_1945


class TestClass1945:
    def test_solution_0(self, init_variables_1945):
        assert init_variables_1945().getLucky("iiii", 1) == 36

    def test_solution_1(self, init_variables_1945):
        assert init_variables_1945().getLucky("leetcode", 2) == 6

    def test_solution_2(self, init_variables_1945):
        assert init_variables_1945().getLucky("zbax", 2) == 8
