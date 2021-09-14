#!/usr/bin/env python

import pytest

"""
Test 98. Validate Binary Search Tree
"""


@pytest.fixture(scope="session")
def init_variables_98():
    from src.leetcode_98_validate_binary_search_tree import Solution

    solution = Solution()

    def _init_variables_98():
        return solution

    yield _init_variables_98


class TestClass98:
    def test_solution_0(self, init_variables_98):
        assert init_variables_98().isValidBST([2, 1, 3])

    def test_solution_1(self, init_variables_98):
        assert not init_variables_98().isValidBST([5, 1, 4, None, None, 3, 6])
