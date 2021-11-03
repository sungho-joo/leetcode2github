#!/usr/bin/env python

import pytest

"""
Test 743. Network Delay Time
"""


@pytest.fixture(scope="session")
def init_variables_743():
    from src.leetcode_743_network_delay_time import Solution

    solution = Solution()

    def _init_variables_743():
        return solution

    yield _init_variables_743


class TestClass743:
    def test_solution_0(self, init_variables_743):
        assert init_variables_743().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2

    def test_solution_1(self, init_variables_743):
        assert init_variables_743().networkDelayTime([[1, 2, 1]], 2, 1) == 1

    def test_solution_2(self, init_variables_743):
        assert init_variables_743().networkDelayTime([[1, 2, 1]], 2, 2) == -1
