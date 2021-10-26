#!/usr/bin/env python

import pytest

"""
Test 2038. Remove Colored Pieces if Both Neighbors are the Same Color
"""


@pytest.fixture(scope="session")
def init_variables_2038():
    from src.leetcode_2038_remove_colored_pieces_if_both_neighbors_are_the_same_color import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2038():
        return solution

    yield _init_variables_2038


class TestClass2038:
    def test_solution_0(self, init_variables_2038):
        assert init_variables_2038().winnerOfGame("AAABABB")

    def test_solution_1(self, init_variables_2038):
        assert not init_variables_2038().winnerOfGame("AA")

    def test_solution_2(self, init_variables_2038):
        assert not init_variables_2038().winnerOfGame("ABBBBBBBAAA")
