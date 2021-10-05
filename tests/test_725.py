#!/usr/bin/env python

import pytest

"""
Test 725. Split Linked List in Parts
"""


@pytest.fixture(scope="session")
def init_variables_725():
    from src.leetcode_725_split_linked_list_in_parts import Solution

    solution = Solution()

    def _init_variables_725():
        return solution

    yield _init_variables_725


class TestClass725:
    def test_solution_0(self, init_variables_725):
        assert init_variables_725().splitListToParts([1, 2, 3], 5) == [[1], [2], [3], [], []]

    def test_solution_1(self, init_variables_725):
        assert init_variables_725().splitListToParts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [
            [1, 2, 3, 4],
            [5, 6, 7],
            [8, 9, 10],
        ]
