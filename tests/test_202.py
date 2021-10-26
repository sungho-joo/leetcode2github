#!/usr/bin/env python

import pytest

"""
Test 202. Happy Number
"""


@pytest.fixture(scope="session")
def init_variables_202():
    from src.leetcode_202_happy_number import Solution

    solution = Solution()

    def _init_variables_202():
        return solution

    yield _init_variables_202


class TestClass202:
    def test_solution_0(self, init_variables_202):
        assert init_variables_202().isHappy(19)

    def test_solution_1(self, init_variables_202):
        assert not init_variables_202().isHappy(2)
