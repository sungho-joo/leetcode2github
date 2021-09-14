#!/usr/bin/env python

import pytest

"""
Test 242. Valid Anagram
"""


@pytest.fixture(scope="session")
def init_variables_242():
    from src.leetcode_242_valid_anagram import Solution

    solution = Solution()

    def _init_variables_242():
        return solution

    yield _init_variables_242


class TestClass242:
    def test_solution_0(self, init_variables_242):
        assert init_variables_242().isAnagram("anagram", "nagaram")

    def test_solution_1(self, init_variables_242):
        assert not init_variables_242().isAnagram("rat", "car")
