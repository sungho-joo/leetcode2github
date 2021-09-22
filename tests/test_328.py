#!/usr/bin/env python

import pytest

"""
Test 328. Odd Even Linked List
"""


@pytest.fixture(scope="session")
def init_variables_328():
    from src.leetcode_328_odd_even_linked_list import Solution

    solution = Solution()

    def _init_variables_328():
        return solution

    yield _init_variables_328


class TestClass328:
    def test_solution_0(self, init_variables_328):
        assert init_variables_328().oddEvenList([1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4]

    def test_solution_1(self, init_variables_328):
        assert init_variables_328().oddEvenList([2, 1, 3, 5, 6, 4, 7]) == [2, 3, 6, 7, 1, 5, 4]
