#!/usr/bin/env python

import pytest

"""
Test 809. Expressive Words
"""


@pytest.fixture(scope="session")
def init_variables_809():
    from src.leetcode_809_expressive_words import Solution

    solution = Solution()

    def _init_variables_809():
        return solution

    yield _init_variables_809


class TestClass809:
    def test_solution_0(self, init_variables_809):
        assert init_variables_809().expressiveWords("heeellooo", ["hello", "hi", "helo"]) == 1

    def test_solution_1(self, init_variables_809):
        assert init_variables_809().expressiveWords("zzzzzyyyyy", ["zzyy", "zy", "zyy"]) == 3
