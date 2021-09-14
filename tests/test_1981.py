#!/usr/bin/env python

import pytest

"""
Test 1981. Minimize the Difference Between Target and Chosen Elements
"""


@pytest.fixture(scope="session")
def init_variables_1981():
    from src.leetcode_1981_minimize_the_difference_between_target_and_chosen_elements import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1981():
        return solution

    yield _init_variables_1981


class TestClass1981:
    def test_solution_0(self, init_variables_1981):
        assert init_variables_1981().minimizeTheDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13) == 0

    def test_solution_1(self, init_variables_1981):
        assert init_variables_1981().minimizeTheDifference([[1], [2], [3]], 100) == 94

    def test_solution_2(self, init_variables_1981):
        assert init_variables_1981().minimizeTheDifference([[1, 2, 9, 8, 7]], 6) == 1
