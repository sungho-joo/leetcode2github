#!/usr/bin/env python

import pytest

"""
Test 1953. Maximum Number of Weeks for Which You Can Work
"""


@pytest.fixture(scope="session")
def init_variables_1953():
    from src.leetcode_1953_maximum_number_of_weeks_for_which_you_can_work import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1953():
        return solution

    yield _init_variables_1953


class TestClass1953:
    def test_solution_0(self, init_variables_1953):
        assert init_variables_1953().numberOfWeeks([1, 2, 3]) == 6

    def test_solution_1(self, init_variables_1953):
        assert init_variables_1953().numberOfWeeks([5, 2, 1]) == 7


#!/usr/bin/env python

import pytest

"""
Test 1953. Maximum Number of Weeks for Which You Can Work
"""


@pytest.fixture(scope="session")
def init_variables_1953():
    from src.leetcode_1953_maximum_number_of_weeks_for_which_you_can_work import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1953():
        return solution

    yield _init_variables_1953


class TestClass1953:
    def test_solution_0(self, init_variables_1953):
        assert init_variables_1953().numberOfWeeks([1, 2, 3]) == 6

    def test_solution_1(self, init_variables_1953):
        assert init_variables_1953().numberOfWeeks([5, 2, 1]) == 7
