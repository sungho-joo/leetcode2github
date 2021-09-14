#!/usr/bin/env python

import pytest

"""
Test 927. Three Equal Parts
"""


@pytest.fixture(scope="session")
def init_variables_927():
    from src.leetcode_927_three_equal_parts import Solution

    solution = Solution()

    def _init_variables_927():
        return solution

    yield _init_variables_927


class TestClass927:
    def test_solution_0(self, init_variables_927):
        assert init_variables_927().threeEqualParts([1, 0, 1, 0, 1]) == [0, 3]

    def test_solution_1(self, init_variables_927):
        assert init_variables_927().threeEqualParts([1, 1, 0, 1, 1]) == [-1, -1]

    def test_solution_2(self, init_variables_927):
        assert init_variables_927().threeEqualParts([1, 1, 0, 0, 1]) == [0, 2]


#!/usr/bin/env python

import pytest

"""
Test 927. Three Equal Parts
"""


@pytest.fixture(scope="session")
def init_variables_927():
    from src.leetcode_927_three_equal_parts import Solution

    solution = Solution()

    def _init_variables_927():
        return solution

    yield _init_variables_927


class TestClass927:
    def test_solution_0(self, init_variables_927):
        assert init_variables_927().threeEqualParts([1, 0, 1, 0, 1]) == [0, 3]

    def test_solution_1(self, init_variables_927):
        assert init_variables_927().threeEqualParts([1, 1, 0, 1, 1]) == [-1, -1]

    def test_solution_2(self, init_variables_927):
        assert init_variables_927().threeEqualParts([1, 1, 0, 0, 1]) == [0, 2]
