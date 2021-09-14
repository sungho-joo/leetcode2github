#!/usr/bin/env python

import pytest

"""
Test 1947. Maximum Compatibility Score Sum
"""


@pytest.fixture(scope="session")
def init_variables_1947():
    from src.leetcode_1947_maximum_compatibility_score_sum import Solution

    solution = Solution()

    def _init_variables_1947():
        return solution

    yield _init_variables_1947


class TestClass1947:
    def test_solution_0(self, init_variables_1947):
        assert (
            init_variables_1947().maxCompatibilitySum(
                [[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
            )
            == 8
        )

    def test_solution_1(self, init_variables_1947):
        assert (
            init_variables_1947().maxCompatibilitySum(
                [[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]
            )
            == 0
        )


#!/usr/bin/env python

import pytest

"""
Test 1947. Maximum Compatibility Score Sum
"""


@pytest.fixture(scope="session")
def init_variables_1947():
    from src.leetcode_1947_maximum_compatibility_score_sum import Solution

    solution = Solution()

    def _init_variables_1947():
        return solution

    yield _init_variables_1947


class TestClass1947:
    def test_solution_0(self, init_variables_1947):
        assert (
            init_variables_1947().maxCompatibilitySum(
                [[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
            )
            == 8
        )

    def test_solution_1(self, init_variables_1947):
        assert (
            init_variables_1947().maxCompatibilitySum(
                [[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]
            )
            == 0
        )
