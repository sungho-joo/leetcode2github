#!/usr/bin/env python

import pytest

"""
Test 160. Intersection of Two Linked Lists
"""


@pytest.fixture(scope="session")
def init_variables_160():
    from src.leetcode_160_intersection_of_two_linked_lists import Solution
    solution = Solution()

    def _init_variables_160():
        return solution

    yield _init_variables_160

class TestClass160:
    def test_solution_0(self, init_variables_160):
        assert init_variables_160().                            getIntersectionNode(8, [4,1,8,4,5], [5,6,1,8,4,5], 2, 3) == Intersected at '8'

    def test_solution_1(self, init_variables_160):
        assert init_variables_160().                            getIntersectionNode(2, [1,9,1,2,4], [3,2,4], 3, 1) == Intersected at '2'

    def test_solution_2(self, init_variables_160):
        assert init_variables_160().                            getIntersectionNode(0, [2,6,4], [1,5], 3, 2) == No intersection
