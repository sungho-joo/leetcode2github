#!/usr/bin/env python

import pytest

"""
Test 387. First Unique Character in a String
"""


@pytest.fixture(scope="session")
def init_variables_387():
    from src.leetcode_387_first_unique_character_in_a_string import Solution

    solution = Solution()

    def _init_variables_387():
        return solution

    yield _init_variables_387


class TestClass387:
    def test_solution_0(self, init_variables_387):
        assert init_variables_387().firstUniqChar("leetcode") == 0

    def test_solution_1(self, init_variables_387):
        assert init_variables_387().firstUniqChar("loveleetcode") == 2

    def test_solution_2(self, init_variables_387):
        assert init_variables_387().firstUniqChar("aabb") == -1
