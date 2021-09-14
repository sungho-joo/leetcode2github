#!/usr/bin/env python

import pytest

"""
Test 1866. Number of Ways to Rearrange Sticks With K Sticks Visible
"""


@pytest.fixture(scope="session")
def init_variables_1866():
    from src.leetcode_1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1866():
        return solution

    yield _init_variables_1866


class TestClass1866:
    def test_solution_0(self, init_variables_1866):
        assert init_variables_1866().rearrangeSticks(3, 2) == 3

    def test_solution_1(self, init_variables_1866):
        assert init_variables_1866().rearrangeSticks(5, 5) == 1

    def test_solution_2(self, init_variables_1866):
        assert init_variables_1866().rearrangeSticks(20, 11) == 647427950


#!/usr/bin/env python

import pytest

"""
Test 1866. Number of Ways to Rearrange Sticks With K Sticks Visible
"""


@pytest.fixture(scope="session")
def init_variables_1866():
    from src.leetcode_1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1866():
        return solution

    yield _init_variables_1866


class TestClass1866:
    def test_solution_0(self, init_variables_1866):
        assert init_variables_1866().rearrangeSticks(3, 2) == 3

    def test_solution_1(self, init_variables_1866):
        assert init_variables_1866().rearrangeSticks(5, 5) == 1

    def test_solution_2(self, init_variables_1866):
        assert init_variables_1866().rearrangeSticks(20, 11) == 647427950
