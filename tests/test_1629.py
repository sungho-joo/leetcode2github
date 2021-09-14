#!/usr/bin/env python

import pytest

"""
Test 1629. Slowest Key
"""


@pytest.fixture(scope="session")
def init_variables_1629():
    from src.leetcode_1629_slowest_key import Solution

    solution = Solution()

    def _init_variables_1629():
        return solution

    yield _init_variables_1629


class TestClass1629:
    def test_solution_0(self, init_variables_1629):
        assert init_variables_1629().slowestKey([9, 29, 49, 50], "cbcd") == "c"

    def test_solution_1(self, init_variables_1629):
        assert init_variables_1629().slowestKey([12, 23, 36, 46, 62], "spuda") == "a"
