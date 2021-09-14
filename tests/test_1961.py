#!/usr/bin/env python

import pytest

"""
Test 1961. Check If String Is a Prefix of Array
"""


@pytest.fixture(scope="session")
def init_variables_1961():
    from src.leetcode_1961_check_if_string_is_a_prefix_of_array import Solution

    solution = Solution()

    def _init_variables_1961():
        return solution

    yield _init_variables_1961


class TestClass1961:
    def test_solution_0(self, init_variables_1961):
        assert init_variables_1961().isPrefixString(
            "iloveleetcode", ["i", "love", "leetcode", "apples"]
        )

    def test_solution_1(self, init_variables_1961):
        assert not init_variables_1961().isPrefixString(
            "iloveleetcode", ["apples", "i", "love", "leetcode"]
        )


#!/usr/bin/env python

import pytest

"""
Test 1961. Check If String Is a Prefix of Array
"""


@pytest.fixture(scope="session")
def init_variables_1961():
    from src.leetcode_1961_check_if_string_is_a_prefix_of_array import Solution

    solution = Solution()

    def _init_variables_1961():
        return solution

    yield _init_variables_1961


class TestClass1961:
    def test_solution_0(self, init_variables_1961):
        assert init_variables_1961().isPrefixString(
            "iloveleetcode", ["i", "love", "leetcode", "apples"]
        )

    def test_solution_1(self, init_variables_1961):
        assert not init_variables_1961().isPrefixString(
            "iloveleetcode", ["apples", "i", "love", "leetcode"]
        )
