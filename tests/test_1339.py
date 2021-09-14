#!/usr/bin/env python

import pytest

"""
Test 1339. Maximum Product of Splitted Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_1339():
    from src.leetcode_1339_maximum_product_of_splitted_binary_tree import Solution

    solution = Solution()

    def _init_variables_1339():
        return solution

    yield _init_variables_1339


class TestClass1339:
    def test_solution_0(self, init_variables_1339):
        assert init_variables_1339().maxProduct([1, 2, 3, 4, 5, 6]) == 110

    def test_solution_1(self, init_variables_1339):
        assert init_variables_1339().maxProduct([1, None, 2, 3, 4, None, None, 5, 6]) == 90

    def test_solution_2(self, init_variables_1339):
        assert init_variables_1339().maxProduct([2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1]) == 1025

    def test_solution_3(self, init_variables_1339):
        assert init_variables_1339().maxProduct([1, 1]) == 1
