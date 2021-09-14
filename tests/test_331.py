#!/usr/bin/env python

import pytest

"""
Test 331. Verify Preorder Serialization of a Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_331():
    from src.leetcode_331_verify_preorder_serialization_of_a_binary_tree import Solution

    solution = Solution()

    def _init_variables_331():
        return solution

    yield _init_variables_331


class TestClass331:
    def test_solution_0(self, init_variables_331):
        assert init_variables_331().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")

    def test_solution_1(self, init_variables_331):
        assert not init_variables_331().isValidSerialization("1,#")

    def test_solution_2(self, init_variables_331):
        assert not init_variables_331().isValidSerialization("9,#,#,1")
