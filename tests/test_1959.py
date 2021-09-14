#!/usr/bin/env python

import pytest

"""
Test 1959. Minimum Total Space Wasted With K Resizing Operations
"""


@pytest.fixture(scope="session")
def init_variables_1959():
    from src.leetcode_1959_minimum_total_space_wasted_with_k_resizing_operations import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1959():
        return solution

    yield _init_variables_1959


class TestClass1959:
    def test_solution_0(self, init_variables_1959):
        assert init_variables_1959().minSpaceWastedKResizing([10, 20], 0) == 10

    def test_solution_1(self, init_variables_1959):
        assert init_variables_1959().minSpaceWastedKResizing([10, 20, 30], 1) == 10

    def test_solution_2(self, init_variables_1959):
        assert init_variables_1959().minSpaceWastedKResizing([10, 20, 15, 30, 20], 2) == 15


#!/usr/bin/env python

import pytest

"""
Test 1959. Minimum Total Space Wasted With K Resizing Operations
"""


@pytest.fixture(scope="session")
def init_variables_1959():
    from src.leetcode_1959_minimum_total_space_wasted_with_k_resizing_operations import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1959():
        return solution

    yield _init_variables_1959


class TestClass1959:
    def test_solution_0(self, init_variables_1959):
        assert init_variables_1959().minSpaceWastedKResizing([10, 20], 0) == 10

    def test_solution_1(self, init_variables_1959):
        assert init_variables_1959().minSpaceWastedKResizing([10, 20, 30], 1) == 10

    def test_solution_2(self, init_variables_1959):
        assert init_variables_1959().minSpaceWastedKResizing([10, 20, 15, 30, 20], 2) == 15
