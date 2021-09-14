#!/usr/bin/env python

import pytest

"""
Test 848. Shifting Letters
"""


@pytest.fixture(scope="session")
def init_variables_848():
    from src.leetcode_848_shifting_letters import Solution

    solution = Solution()

    def _init_variables_848():
        return solution

    yield _init_variables_848


class TestClass848:
    def test_solution_0(self, init_variables_848):
        assert init_variables_848().shiftingLetters("abc", [3, 5, 9]) == "rpl"

    def test_solution_1(self, init_variables_848):
        assert init_variables_848().shiftingLetters("aaa", [1, 2, 3]) == "gfd"
