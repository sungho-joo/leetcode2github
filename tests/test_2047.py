#!/usr/bin/env python

import pytest

"""
Test 2047. Number of Valid Words in a Sentence
"""


@pytest.fixture(scope="session")
def init_variables_2047():
    from src.leetcode_2047_number_of_valid_words_in_a_sentence import Solution

    solution = Solution()

    def _init_variables_2047():
        return solution

    yield _init_variables_2047


class TestClass2047:
    def test_solution_0(self, init_variables_2047):
        assert init_variables_2047().countValidWords("cat and  dog") == 3

    def test_solution_1(self, init_variables_2047):
        assert init_variables_2047().countValidWords("!this  1-s b8d!") == 0

    def test_solution_2(self, init_variables_2047):
        assert init_variables_2047().countValidWords("alice and  bob are playing stone-game10") == 5

    def test_solution_3(self, init_variables_2047):
        assert (
            init_variables_2047().countValidWords(
                "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
            )
            == 6
        )
