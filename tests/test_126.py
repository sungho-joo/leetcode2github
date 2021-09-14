#!/usr/bin/env python

import pytest

"""
Test 126. Word Ladder II
"""


@pytest.fixture(scope="session")
def init_variables_126():
    from src.leetcode_126_word_ladder_ii import Solution

    solution = Solution()

    def _init_variables_126():
        return solution

    yield _init_variables_126


class TestClass126:
    def test_solution_0(self, init_variables_126):
        assert init_variables_126().findLadders(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        ) == [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]

    def test_solution_1(self, init_variables_126):
        assert init_variables_126().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == []


#!/usr/bin/env python

import pytest

"""
Test 126. Word Ladder II
"""


@pytest.fixture(scope="session")
def init_variables_126():
    from src.leetcode_126_word_ladder_ii import Solution

    solution = Solution()

    def _init_variables_126():
        return solution

    yield _init_variables_126


class TestClass126:
    def test_solution_0(self, init_variables_126):
        assert init_variables_126().findLadders(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        ) == [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]

    def test_solution_1(self, init_variables_126):
        assert init_variables_126().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == []
