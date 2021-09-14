#!/usr/bin/env python

import pytest

"""
Test 1969. Minimum Non-Zero Product of the Array Elements
"""


@pytest.fixture(scope="session")
def init_variables_1969():
    from src.leetcode_1969_minimum_non_zero_product_of_the_array_elements import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1969():
        return solution

    yield _init_variables_1969


class TestClass1969:
    def test_solution_0(self, init_variables_1969):
        assert init_variables_1969().minNonZeroProduct(1) == 1

    def test_solution_1(self, init_variables_1969):
        assert init_variables_1969().minNonZeroProduct(2) == 6

    def test_solution_2(self, init_variables_1969):
        assert init_variables_1969().minNonZeroProduct(3) == 1512


#!/usr/bin/env python

import pytest

"""
Test 1969. Minimum Non-Zero Product of the Array Elements
"""


@pytest.fixture(scope="session")
def init_variables_1969():
    from src.leetcode_1969_minimum_non_zero_product_of_the_array_elements import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1969():
        return solution

    yield _init_variables_1969


class TestClass1969:
    def test_solution_0(self, init_variables_1969):
        assert init_variables_1969().minNonZeroProduct(1) == 1

    def test_solution_1(self, init_variables_1969):
        assert init_variables_1969().minNonZeroProduct(2) == 6

    def test_solution_2(self, init_variables_1969):
        assert init_variables_1969().minNonZeroProduct(3) == 1512
