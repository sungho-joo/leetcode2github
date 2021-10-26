#!/usr/bin/env python

import pytest

"""
Test 212. Word Search II
"""


@pytest.fixture(scope="session")
def init_variables_212():
    from src.leetcode_212_word_search_ii import Solution

    solution = Solution()

    def _init_variables_212():
        return solution

    yield _init_variables_212


class TestClass212:
    def test_solution_0(self, init_variables_212):
        assert (
            init_variables_212().findWords(
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                ["oath", "pea", "eat", "rain"],
            )
            == ["eat", "oath"]
        )

    def test_solution_1(self, init_variables_212):
        assert init_variables_212().findWords([["a", "b"], ["c", "d"]], ["abcb"]) == []
