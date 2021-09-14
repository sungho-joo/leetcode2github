#!/usr/bin/env python

import pytest

"""
Test 598. Range Addition II
"""


@pytest.fixture(scope="session")
def init_variables_598():
    from src.leetcode_598_range_addition_ii import Solution

    solution = Solution()

    def _init_variables_598():
        return solution

    yield _init_variables_598


class TestClass598:
    def test_solution_0(self, init_variables_598):
        assert init_variables_598().maxCount(3, 3, [[2, 2], [3, 3]]) == 4

    def test_solution_1(self, init_variables_598):
        assert (
            init_variables_598().maxCount(
                3,
                3,
                [
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                ],
            )
            == 4
        )

    def test_solution_2(self, init_variables_598):
        assert init_variables_598().maxCount(3, 3, []) == 9
