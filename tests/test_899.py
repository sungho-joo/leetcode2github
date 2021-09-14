#!/usr/bin/env python

import pytest

"""
Test 899. Orderly Queue
"""


@pytest.fixture(scope="session")
def init_variables_899():
    from src.leetcode_899_orderly_queue import Solution

    solution = Solution()

    def _init_variables_899():
        return solution

    yield _init_variables_899


class TestClass899:
    def test_solution_0(self, init_variables_899):
        assert init_variables_899().orderlyQueue("cba", 1) == "acb"

    def test_solution_1(self, init_variables_899):
        assert init_variables_899().orderlyQueue("baaca", 3) == "aaabc"
