#!/usr/bin/env python

import pytest

"""
Test 1275. Find Winner on a Tic Tac Toe Game
"""


@pytest.fixture(scope="session")
def init_variables_1275():
    from src.leetcode_1275_find_winner_on_a_tic_tac_toe_game import Solution

    solution = Solution()

    def _init_variables_1275():
        return solution

    yield _init_variables_1275


class TestClass1275:
    def test_solution_0(self, init_variables_1275):
        assert init_variables_1275().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == "A"

    def test_solution_1(self, init_variables_1275):
        assert init_variables_1275().tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == "B"

    def test_solution_2(self, init_variables_1275):
        assert (
            init_variables_1275().tictactoe(
                [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
            )
            == "Draw"
        )

    def test_solution_3(self, init_variables_1275):
        assert init_variables_1275().tictactoe([[0, 0], [1, 1]]) == "Pending"
