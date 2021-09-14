#!/usr/bin/env python

import pytest

"""
Test 1816. Truncate Sentence
"""


@pytest.fixture(scope="session")
def init_variables_1816():
    from src.leetcode_1816_truncate_sentence import Solution

    solution = Solution()

    def _init_variables_1816():
        return solution

    yield _init_variables_1816


class TestClass1816:
    def test_solution_0(self, init_variables_1816):
        assert (
            init_variables_1816().truncateSentence("Hello how are you Contestant", 4)
            == "Hello how are you"
        )

    def test_solution_1(self, init_variables_1816):
        assert (
            init_variables_1816().truncateSentence("What is the solution to this problem", 4)
            == "What is the solution"
        )

    def test_solution_2(self, init_variables_1816):
        assert (
            init_variables_1816().truncateSentence("chopper is not a tanuki", 5)
            == "chopper is not a tanuki"
        )
