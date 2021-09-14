#!/usr/bin/env python

import pytest

"""
Test 1963. Minimum Number of Swaps to Make the String Balanced
"""


@pytest.fixture(scope="session")
def init_variables_1963():
    from src.leetcode_1963_minimum_number_of_swaps_to_make_the_string_balanced import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1963():
        return solution

    yield _init_variables_1963


class TestClass1963:
    def test_solution_0(self, init_variables_1963):
        assert init_variables_1963().minSwaps("][][") == 1

    def test_solution_1(self, init_variables_1963):
        assert init_variables_1963().minSwaps("]]][[[") == 2

    def test_solution_2(self, init_variables_1963):
        assert init_variables_1963().minSwaps("[]") == 0


#!/usr/bin/env python

import pytest

"""
Test 1963. Minimum Number of Swaps to Make the String Balanced
"""


@pytest.fixture(scope="session")
def init_variables_1963():
    from src.leetcode_1963_minimum_number_of_swaps_to_make_the_string_balanced import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1963():
        return solution

    yield _init_variables_1963


class TestClass1963:
    def test_solution_0(self, init_variables_1963):
        assert init_variables_1963().minSwaps("][][") == 1

    def test_solution_1(self, init_variables_1963):
        assert init_variables_1963().minSwaps("]]][[[") == 2

    def test_solution_2(self, init_variables_1963):
        assert init_variables_1963().minSwaps("[]") == 0
