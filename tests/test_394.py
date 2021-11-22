#!/usr/bin/env python

import pytest

"""
Test 394. Decode String
"""


@pytest.fixture(scope="session")
def init_variables_394():
    from src.leetcode_394_decode_string import Solution

    solution = Solution()

    def _init_variables_394():
        return solution

    yield _init_variables_394


class TestClass394:
    def test_solution_0(self, init_variables_394):
        assert init_variables_394().decodeString("3[a]2[bc]") == "aaabcbc"

    def test_solution_1(self, init_variables_394):
        assert init_variables_394().decodeString("3[a2[c]]") == "accaccacc"

    def test_solution_2(self, init_variables_394):
        assert init_variables_394().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"

    def test_solution_3(self, init_variables_394):
        assert init_variables_394().decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
