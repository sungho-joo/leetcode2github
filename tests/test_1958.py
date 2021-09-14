#!/usr/bin/env python

import pytest

"""
Test 1958. Check if Move is Legal
"""


@pytest.fixture(scope="session")
def init_variables_1958():
    from src.leetcode_1958_check_if_move_is_legal import Solution

    solution = Solution()

    def _init_variables_1958():
        return solution

    yield _init_variables_1958


class TestClass1958:
    def test_solution_0(self, init_variables_1958):
        assert init_variables_1958().checkMove(
            [
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                ["W", "B", "B", ".", "W", "W", "W", "B"],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
            ],
            4,
            3,
            "B",
        )

    def test_solution_1(self, init_variables_1958):
        assert not init_variables_1958().checkMove(
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "B", ".", ".", "W", ".", ".", "."],
                [".", ".", "W", ".", ".", ".", ".", "."],
                [".", ".", ".", "W", "B", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "B", "W", ".", "."],
                [".", ".", ".", ".", ".", ".", "W", "."],
                [".", ".", ".", ".", ".", ".", ".", "B"],
            ],
            4,
            4,
            "W",
        )


#!/usr/bin/env python

import pytest

"""
Test 1958. Check if Move is Legal
"""


@pytest.fixture(scope="session")
def init_variables_1958():
    from src.leetcode_1958_check_if_move_is_legal import Solution

    solution = Solution()

    def _init_variables_1958():
        return solution

    yield _init_variables_1958


class TestClass1958:
    def test_solution_0(self, init_variables_1958):
        assert init_variables_1958().checkMove(
            [
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                ["W", "B", "B", ".", "W", "W", "W", "B"],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
            ],
            4,
            3,
            "B",
        )

    def test_solution_1(self, init_variables_1958):
        assert not init_variables_1958().checkMove(
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "B", ".", ".", "W", ".", ".", "."],
                [".", ".", "W", ".", ".", ".", ".", "."],
                [".", ".", ".", "W", "B", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "B", "W", ".", "."],
                [".", ".", ".", ".", ".", ".", "W", "."],
                [".", ".", ".", ".", ".", ".", ".", "B"],
            ],
            4,
            4,
            "W",
        )
