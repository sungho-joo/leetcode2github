#!/usr/bin/env python

import pytest

"""
Test 151. Reverse Words in a String
"""


@pytest.fixture(scope="session")
def init_variables_151():
    from src.leetcode_151_reverse_words_in_a_string import Solution

    solution = Solution()

    def _init_variables_151():
        return solution

    yield _init_variables_151


class TestClass151:
    def test_solution_0(self, init_variables_151):
        assert init_variables_151().reverseWords("the sky is blue") == "blue is sky the"

    def test_solution_1(self, init_variables_151):
        assert init_variables_151().reverseWords("  hello world  ") == "world hello"

    def test_solution_2(self, init_variables_151):
        assert init_variables_151().reverseWords("a good   example") == "example good a"

    def test_solution_3(self, init_variables_151):
        assert init_variables_151().reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"

    def test_solution_4(self, init_variables_151):
        assert (
            init_variables_151().reverseWords("Alice does not even like bob")
            == "bob like even not does Alice"
        )
