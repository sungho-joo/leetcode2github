#!/usr/bin/env python

import pytest

"""
Test 1286. Iterator for Combination
"""


@pytest.fixture(scope="session")
def init_variables_1286():
    from src.leetcode_1286_iterator_for_combination import Solution

    solution = Solution()

    def _init_variables_1286():
        return solution

    yield _init_variables_1286


class TestClass1286:
    def test_solution_0(self, init_variables_1286):
        assert (
            init_variables_1286().CombinationIterator(
                ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
                [["abc", 2], [], [], [], [], [], []],
            )
            == [None, "ab", True, "ac", True, "bc", False]
        )
