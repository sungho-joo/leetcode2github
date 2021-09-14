#!/usr/bin/env python

import pytest

"""
Test 1888. Minimum Number of Flips to Make the Binary String Alternating
"""


@pytest.fixture(scope="session")
def init_variables_1888():
    from src.leetcode_1888_minimum_number_of_flips_to_make_the_binary_string_alternating import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1888():
        return solution

    yield _init_variables_1888


class TestClass1888:
    def test_solution_0(self, init_variables_1888):
        assert init_variables_1888().minFlips("111000") == 2

    def test_solution_1(self, init_variables_1888):
        assert init_variables_1888().minFlips("010") == 0

    def test_solution_2(self, init_variables_1888):
        assert init_variables_1888().minFlips("1110") == 1


#!/usr/bin/env python

import pytest

"""
Test 1888. Minimum Number of Flips to Make the Binary String Alternating
"""


@pytest.fixture(scope="session")
def init_variables_1888():
    from src.leetcode_1888_minimum_number_of_flips_to_make_the_binary_string_alternating import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1888():
        return solution

    yield _init_variables_1888


class TestClass1888:
    def test_solution_0(self, init_variables_1888):
        assert init_variables_1888().minFlips("111000") == 2

    def test_solution_1(self, init_variables_1888):
        assert init_variables_1888().minFlips("010") == 0

    def test_solution_2(self, init_variables_1888):
        assert init_variables_1888().minFlips("1110") == 1
