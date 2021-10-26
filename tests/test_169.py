#!/usr/bin/env python

import pytest

"""
Test 169. Majority Element
"""


@pytest.fixture(scope="session")
def init_variables_169():
    from src.leetcode_169_majority_element import Solution

    solution = Solution()

    def _init_variables_169():
        return solution

    yield _init_variables_169


class TestClass169:
    def test_solution_0(self, init_variables_169):
        assert init_variables_169().majorityElement([3, 2, 3]) == 3

    def test_solution_1(self, init_variables_169):
        assert init_variables_169().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
