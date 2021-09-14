#!/usr/bin/env python

import pytest

"""
Test 344. Reverse String
"""


@pytest.fixture(scope="session")
def init_variables_344():
    from src.leetcode_344_reverse_string import Solution

    solution = Solution()

    def _init_variables_344():
        return solution

    yield _init_variables_344


class TestClass344:
    def test_solution_0(self, init_variables_344):
        assert init_variables_344().reverseString(["h", "e", "l", "l", "o"]) == [
            "o",
            "l",
            "l",
            "e",
            "h",
        ]

    def test_solution_1(self, init_variables_344):
        assert init_variables_344().reverseString(["H", "a", "n", "n", "a", "h"]) == [
            "h",
            "a",
            "n",
            "n",
            "a",
            "H",
        ]
