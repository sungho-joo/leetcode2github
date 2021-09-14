#!/usr/bin/env python

import pytest

"""
Test 155. Min Stack
"""


@pytest.fixture(scope="session")
def init_variables_155():
    from src.leetcode_155_min_stack import Solution

    solution = Solution()

    def _init_variables_155():
        return solution

    yield _init_variables_155


class TestClass155:
    def test_solution_0(self, init_variables_155):
        assert (
            init_variables_155().push(
                ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []],
            )
            == [None, None, None, None, -3, None, 0, -2]
        )
