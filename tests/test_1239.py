#!/usr/bin/env python

import pytest

"""
Test 1239. Maximum Length of a Concatenated String with Unique Characters
"""


@pytest.fixture(scope="session")
def init_variables_1239():
    from src.leetcode_1239_maximum_length_of_a_concatenated_string_with_unique_characters import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1239():
        return solution

    yield _init_variables_1239


class TestClass1239:
    def test_solution_0(self, init_variables_1239):
        assert init_variables_1239().maxLength(["un", "iq", "ue"]) == 4

    def test_solution_1(self, init_variables_1239):
        assert init_variables_1239().maxLength(["cha", "r", "act", "ers"]) == 6

    def test_solution_2(self, init_variables_1239):
        assert init_variables_1239().maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26
