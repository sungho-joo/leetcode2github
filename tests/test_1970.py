#!/usr/bin/env python

import pytest

"""
Test 1970. Last Day Where You Can Still Cross
"""


@pytest.fixture(scope="session")
def init_variables_1970():
    from src.leetcode_1970_last_day_where_you_can_still_cross import Solution

    solution = Solution()

    def _init_variables_1970():
        return solution

    yield _init_variables_1970


class TestClass1970:
    def test_solution_0(self, init_variables_1970):
        assert init_variables_1970().latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]) == 2

    def test_solution_1(self, init_variables_1970):
        assert init_variables_1970().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1

    def test_solution_2(self, init_variables_1970):
        assert (
            init_variables_1970().latestDayToCross(
                3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
            )
            == 3
        )


#!/usr/bin/env python

import pytest

"""
Test 1970. Last Day Where You Can Still Cross
"""


@pytest.fixture(scope="session")
def init_variables_1970():
    from src.leetcode_1970_last_day_where_you_can_still_cross import Solution

    solution = Solution()

    def _init_variables_1970():
        return solution

    yield _init_variables_1970


class TestClass1970:
    def test_solution_0(self, init_variables_1970):
        assert init_variables_1970().latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]) == 2

    def test_solution_1(self, init_variables_1970):
        assert init_variables_1970().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1

    def test_solution_2(self, init_variables_1970):
        assert (
            init_variables_1970().latestDayToCross(
                3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
            )
            == 3
        )
