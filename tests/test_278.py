#!/usr/bin/env python

import pytest

"""
Test 278. First Bad Version
"""


@pytest.fixture(scope="session")
def init_variables_278():
    from src.leetcode_278_first_bad_version import Solution

    solution = Solution()

    def _init_variables_278():
        return solution

    yield _init_variables_278


class TestClass278:
    def test_solution_0(self, init_variables_278):
        assert init_variables_278().firstBadVersion(5, 4) == 4

    def test_solution_1(self, init_variables_278):
        assert init_variables_278().firstBadVersion(1, 1) == 1
