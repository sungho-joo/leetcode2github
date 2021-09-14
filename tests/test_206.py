#!/usr/bin/env python

import pytest

"""
Test 206. Reverse Linked List
"""


@pytest.fixture(scope="session")
def init_variables_206():
    from src.leetcode_206_reverse_linked_list import Solution

    solution = Solution()

    def _init_variables_206():
        return solution

    yield _init_variables_206


class TestClass206:
    def test_solution_0(self, init_variables_206):
        assert init_variables_206().reverseList([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    def test_solution_1(self, init_variables_206):
        assert init_variables_206().reverseList([1, 2]) == [2, 1]

    def test_solution_2(self, init_variables_206):
        assert init_variables_206().reverseList([]) == []
