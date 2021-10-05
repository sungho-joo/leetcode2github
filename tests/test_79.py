#!/usr/bin/env python

import pytest

"""
Test 79. Word Search
"""


@pytest.fixture(scope="session")
def init_variables_79():
    from src.leetcode_79_word_search import Solution

    solution = Solution()

    def _init_variables_79():
        return solution

    yield _init_variables_79


class TestClass79:
    def test_solution_0(self, init_variables_79):
        assert init_variables_79().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )

    def test_solution_1(self, init_variables_79):
        assert init_variables_79().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )

    def test_solution_2(self, init_variables_79):
        assert not init_variables_79().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
