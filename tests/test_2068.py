#!/usr/bin/env python

import pytest

"""
Test 2068. Check Whether Two Strings are Almost Equivalent
"""


@pytest.fixture(scope="session")
def init_variables_2068():
    from src.leetcode_2068_check_whether_two_strings_are_almost_equivalent import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2068():
        return solution

    yield _init_variables_2068


class TestClass2068:
    def test_solution_0(self, init_variables_2068):
        assert not init_variables_2068().checkAlmostEquivalent("aaaa", "bccb")

    def test_solution_1(self, init_variables_2068):
        assert init_variables_2068().checkAlmostEquivalent("abcdeef", "abaaacc")

    def test_solution_2(self, init_variables_2068):
        assert init_variables_2068().checkAlmostEquivalent("cccddabba", "babababab")
