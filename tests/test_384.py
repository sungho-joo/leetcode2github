#!/usr/bin/env python

import pytest

"""
Test 384. Shuffle an Array
"""


@pytest.fixture(scope="session")
def init_variables_384():
    from src.leetcode_384_shuffle_an_array import Solution

    solution = Solution()

    def _init_variables_384():
        return solution

    yield _init_variables_384


class TestClass384:
    def test_solution_0(self, init_variables_384):
        assert init_variables_384().Solution(
            ["Solution", "shuffle", "reset", "shuffle"], [[[1, 2, 3]], [], [], []]
        ) == [None, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
