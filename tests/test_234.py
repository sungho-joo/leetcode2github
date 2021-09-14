#!/usr/bin/env python

import pytest

"""
Test 234. Palindrome Linked List
"""


@pytest.fixture(scope="session")
def init_variables_234():
    from src.leetcode_234_palindrome_linked_list import Solution

    solution = Solution()

    def _init_variables_234():
        return solution

    yield _init_variables_234


class TestClass234:
    def test_solution_0(self, init_variables_234):
        assert init_variables_234().isPalindrome([1, 2, 2, 1])

    def test_solution_1(self, init_variables_234):
        assert not init_variables_234().isPalindrome([1, 2])
