#!/usr/bin/env python

import pytest

"""
Test 1189. Maximum Number of Balloons
"""


@pytest.fixture(scope="session")
def init_variables_1189():
    from src.leetcode_1189_maximum_number_of_balloons import Solution

    solution = Solution()

    def _init_variables_1189():
        return solution

    yield _init_variables_1189


class TestClass1189:
    def test_solution_0(self, init_variables_1189):
        assert init_variables_1189().maxNumberOfBalloons("nlaebolko") == 1

    def test_solution_1(self, init_variables_1189):
        assert init_variables_1189().maxNumberOfBalloons("loonbalxballpoon") == 2

    def test_solution_2(self, init_variables_1189):
        assert init_variables_1189().maxNumberOfBalloons("leetcode") == 0
