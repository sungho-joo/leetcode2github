#!/usr/bin/env python

import pytest

"""
Test 200. Number of Islands
"""


@pytest.fixture(scope="session")
def init_variables_200():
    from src.leetcode_200_number_of_islands import Solution

    solution = Solution()

    def _init_variables_200():
        return solution

    yield _init_variables_200


class TestClass200:
    def test_solution_0(self, init_variables_200):
        assert (
            init_variables_200().numIslands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            )
            == 1
        )

    def test_solution_1(self, init_variables_200):
        assert (
            init_variables_200().numIslands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            )
            == 3
        )
