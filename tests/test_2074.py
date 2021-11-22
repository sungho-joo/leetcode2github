#!/usr/bin/env python

import pytest

"""
Test 2074. Reverse Nodes in Even Length Groups
"""


@pytest.fixture(scope="session")
def init_variables_2074():
    from src.leetcode_2074_reverse_nodes_in_even_length_groups import Solution

    solution = Solution()

    def _init_variables_2074():
        return solution

    yield _init_variables_2074


class TestClass2074:
    def test_solution_0(self, init_variables_2074):
        assert init_variables_2074().reverseEvenLengthGroups([5, 2, 6, 3, 9, 1, 7, 3, 8, 4]) == [
            5,
            6,
            2,
            3,
            9,
            1,
            4,
            8,
            3,
            7,
        ]

    def test_solution_1(self, init_variables_2074):
        assert init_variables_2074().reverseEvenLengthGroups([1, 1, 0, 6]) == [1, 0, 1, 6]

    def test_solution_2(self, init_variables_2074):
        assert init_variables_2074().reverseEvenLengthGroups([1, 1, 0, 6, 5]) == [1, 0, 1, 5, 6]

    def test_solution_3(self, init_variables_2074):
        assert init_variables_2074().reverseEvenLengthGroups([2, 1]) == [2, 1]

    def test_solution_4(self, init_variables_2074):
        assert init_variables_2074().reverseEvenLengthGroups([8]) == [8]
