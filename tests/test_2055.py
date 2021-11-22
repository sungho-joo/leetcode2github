#!/usr/bin/env python

import pytest

"""
Test 2055. Plates Between Candles
"""


@pytest.fixture(scope="session")
def init_variables_2055():
    from src.leetcode_2055_plates_between_candles import Solution

    solution = Solution()

    def _init_variables_2055():
        return solution

    yield _init_variables_2055


class TestClass2055:
    def test_solution_0(self, init_variables_2055):
        assert init_variables_2055().platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]) == [2, 3]

    def test_solution_1(self, init_variables_2055):
        assert init_variables_2055().platesBetweenCandles(
            "***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        ) == [9, 0, 0, 0, 0]
