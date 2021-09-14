#!/usr/bin/env python

import pytest

"""
Test 330. Patching Array
"""


@pytest.fixture(scope="session")
def init_variables_330():
    from src.leetcode_330_patching_array import Solution

    solution = Solution()

    def _init_variables_330():
        return solution

    yield _init_variables_330


class TestClass330:
    def test_solution_0(self, init_variables_330):
        assert init_variables_330().minPatches([1, 3], 6) == 1

    def test_solution_1(self, init_variables_330):
        assert init_variables_330().minPatches([1, 5, 10], 20) == 2

    def test_solution_2(self, init_variables_330):
        assert init_variables_330().minPatches([1, 2, 2], 5) == 0
