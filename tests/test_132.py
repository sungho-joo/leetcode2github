#!/usr/bin/env python

import pytest

"""
Test 132. Palindrome Partitioning II
"""


@pytest.fixture(scope="session")
def init_variables_132():
    from src.leetcode_132_palindrome_partitioning_ii import Solution

    solution = Solution()

    def _init_variables_132():
        return solution

    yield _init_variables_132


class TestClass132:
    def test_solution_0(self, init_variables_132):
        assert init_variables_132().minCut("aab") == 1

    def test_solution_1(self, init_variables_132):
        assert init_variables_132().minCut("a") == 0

    def test_solution_2(self, init_variables_132):
        assert init_variables_132().minCut("ab") == 1


#!/usr/bin/env python

import pytest

"""
Test 132. Palindrome Partitioning II
"""


@pytest.fixture(scope="session")
def init_variables_132():
    from src.leetcode_132_palindrome_partitioning_ii import Solution

    solution = Solution()

    def _init_variables_132():
        return solution

    yield _init_variables_132


class TestClass132:
    def test_solution_0(self, init_variables_132):
        assert init_variables_132().minCut("aab") == 1

    def test_solution_1(self, init_variables_132):
        assert init_variables_132().minCut("a") == 0

    def test_solution_2(self, init_variables_132):
        assert init_variables_132().minCut("ab") == 1
