#!/usr/bin/env python

import pytest

"""
Test 1864. Minimum Number of Swaps to Make the Binary String Alternating
"""


@pytest.fixture(scope="session")
def init_variables_1864():
    from src.leetcode_1864_minimum_number_of_swaps_to_make_the_binary_string_alternating import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1864():
        return solution

    yield _init_variables_1864


class TestClass1864:
    def test_solution_0(self, init_variables_1864):
        assert init_variables_1864().minSwaps("111000") == 1

    def test_solution_1(self, init_variables_1864):
        assert init_variables_1864().minSwaps("010") == 0

    def test_solution_2(self, init_variables_1864):
        assert init_variables_1864().minSwaps("1110") == -1


#!/usr/bin/env python

import pytest

"""
Test 1864. Minimum Number of Swaps to Make the Binary String Alternating
"""


@pytest.fixture(scope="session")
def init_variables_1864():
    from src.leetcode_1864_minimum_number_of_swaps_to_make_the_binary_string_alternating import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1864():
        return solution

    yield _init_variables_1864


class TestClass1864:
    def test_solution_0(self, init_variables_1864):
        assert init_variables_1864().minSwaps("111000") == 1

    def test_solution_1(self, init_variables_1864):
        assert init_variables_1864().minSwaps("010") == 0

    def test_solution_2(self, init_variables_1864):
        assert init_variables_1864().minSwaps("1110") == -1
