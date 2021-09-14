#!/usr/bin/env python

import pytest

"""
Test 77. Combinations
"""


@pytest.fixture(scope="session")
def init_variables_77():
    from src.leetcode_77_combinations import Solution

    solution = Solution()

    def _init_variables_77():
        return solution

    yield _init_variables_77


class TestClass77:
    def test_solution_0(self, init_variables_77):
        assert init_variables_77().combine(4, 2) == [[1]]


#!/usr/bin/env python

import pytest

"""
Test 77. Combinations
"""


@pytest.fixture(scope="session")
def init_variables_77():
    from src.leetcode_77_combinations import Solution

    solution = Solution()

    def _init_variables_77():
        return solution

    yield _init_variables_77


class TestClass77:
    def test_solution_0(self, init_variables_77):
        assert init_variables_77().combine(4, 2) == [[1]]
