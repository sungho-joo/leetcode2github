#!/usr/bin/env python

import pytest

"""
Test 946. Validate Stack Sequences
"""


@pytest.fixture(scope="session")
def init_variables_946():
    from src.leetcode_946_validate_stack_sequences import Solution

    solution = Solution()

    def _init_variables_946():
        return solution

    yield _init_variables_946


class TestClass946:
    def test_solution_0(self, init_variables_946):
        assert init_variables_946().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])

    def test_solution_1(self, init_variables_946):
        assert not init_variables_946().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
