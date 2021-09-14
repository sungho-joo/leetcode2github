#!/usr/bin/env python

import pytest

"""
Test 1704. Determine if String Halves Are Alike
"""


@pytest.fixture(scope="session")
def init_variables_1704():
    from src.leetcode_1704_determine_if_string_halves_are_alike import Solution

    solution = Solution()

    def _init_variables_1704():
        return solution

    yield _init_variables_1704


class TestClass1704:
    def test_solution_0(self, init_variables_1704):
        assert init_variables_1704().halvesAreAlike("book")

    def test_solution_1(self, init_variables_1704):
        assert not init_variables_1704().halvesAreAlike("textbook")

    def test_solution_2(self, init_variables_1704):
        assert not init_variables_1704().halvesAreAlike("MerryChristmas")

    def test_solution_3(self, init_variables_1704):
        assert init_variables_1704().halvesAreAlike("AbCdEfGh")
