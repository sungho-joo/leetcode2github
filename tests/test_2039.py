#!/usr/bin/env python

import pytest

"""
Test 2039. The Time When the Network Becomes Idle
"""


@pytest.fixture(scope="session")
def init_variables_2039():
    from src.leetcode_2039_the_time_when_the_network_becomes_idle import Solution

    solution = Solution()

    def _init_variables_2039():
        return solution

    yield _init_variables_2039


class TestClass2039:
    def test_solution_0(self, init_variables_2039):
        assert init_variables_2039().networkBecomesIdle([[0, 1], [1, 2]], [0, 2, 1]) == 8

    def test_solution_1(self, init_variables_2039):
        assert init_variables_2039().networkBecomesIdle([[0, 1], [0, 2], [1, 2]], [0, 10, 10]) == 3
