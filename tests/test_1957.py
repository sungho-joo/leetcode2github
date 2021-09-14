#!/usr/bin/env python

import pytest

"""
Test 1957. Delete Characters to Make Fancy String
"""


@pytest.fixture(scope="session")
def init_variables_1957():
    from src.leetcode_1957_delete_characters_to_make_fancy_string import Solution

    solution = Solution()

    def _init_variables_1957():
        return solution

    yield _init_variables_1957


class TestClass1957:
    def test_solution_0(self, init_variables_1957):
        assert init_variables_1957().makeFancyString("leeetcode") == "leetcode"

    def test_solution_1(self, init_variables_1957):
        assert init_variables_1957().makeFancyString("aaabaaaa") == "aabaa"

    def test_solution_2(self, init_variables_1957):
        assert init_variables_1957().makeFancyString("aab") == "aab"


#!/usr/bin/env python

import pytest

"""
Test 1957. Delete Characters to Make Fancy String
"""


@pytest.fixture(scope="session")
def init_variables_1957():
    from src.leetcode_1957_delete_characters_to_make_fancy_string import Solution

    solution = Solution()

    def _init_variables_1957():
        return solution

    yield _init_variables_1957


class TestClass1957:
    def test_solution_0(self, init_variables_1957):
        assert init_variables_1957().makeFancyString("leeetcode") == "leetcode"

    def test_solution_1(self, init_variables_1957):
        assert init_variables_1957().makeFancyString("aaabaaaa") == "aabaa"

    def test_solution_2(self, init_variables_1957):
        assert init_variables_1957().makeFancyString("aab") == "aab"
