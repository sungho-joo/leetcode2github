#!/usr/bin/env python

import pytest

"""
Test 1996. The Number of Weak Characters in the Game
"""


@pytest.fixture(scope="session")
def init_variables_1996():
    from src.leetcode_1996_the_number_of_weak_characters_in_the_game import Solution

    solution = Solution()

    def _init_variables_1996():
        return solution

    yield _init_variables_1996


class TestClass1996:
    def test_solution_0(self, init_variables_1996):
        assert init_variables_1996().numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0

    def test_solution_1(self, init_variables_1996):
        assert init_variables_1996().numberOfWeakCharacters([[2, 2], [3, 3]]) == 1

    def test_solution_2(self, init_variables_1996):
        assert init_variables_1996().numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]) == 1
