#!/usr/bin/env python

import pytest

"""
Test 843. Guess the Word
"""


@pytest.fixture(scope="session")
def init_variables_843():
    from src.leetcode_843_guess_the_word import Solution
    solution = Solution()

    def _init_variables_843():
        return solution

    yield _init_variables_843

class TestClass843:
    def test_solution_0(self, init_variables_843):
        assert init_variables_843().                            findSecretWord("acckzz", ["acckzz","ccbazz","eiowzz","abcczz"], 10) == You guessed the secret word correctly.

    def test_solution_1(self, init_variables_843):
        assert init_variables_843().                            findSecretWord("hamada", ["hamada","khaled"], 10) == You guessed the secret word correctly.
