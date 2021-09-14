#!/usr/bin/env python

import pytest

"""
Test 1943. Describe the Painting
"""


@pytest.fixture(scope="session")
def init_variables_1943():
    from src.leetcode_1943_describe_the_painting import Solution

    solution = Solution()

    def _init_variables_1943():
        return solution

    yield _init_variables_1943


class TestClass1943:
    def test_solution_0(self, init_variables_1943):
        assert init_variables_1943().splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [
            [1, 4, 14],
            [4, 7, 16],
        ]

    def test_solution_1(self, init_variables_1943):
        assert init_variables_1943().splitPainting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]) == [
            [1, 6, 9],
            [6, 7, 24],
            [7, 8, 15],
            [8, 10, 7],
        ]

    def test_solution_2(self, init_variables_1943):
        assert init_variables_1943().splitPainting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]) == [
            [1, 4, 12],
            [4, 7, 12],
        ]


#!/usr/bin/env python

import pytest

"""
Test 1943. Describe the Painting
"""


@pytest.fixture(scope="session")
def init_variables_1943():
    from src.leetcode_1943_describe_the_painting import Solution

    solution = Solution()

    def _init_variables_1943():
        return solution

    yield _init_variables_1943


class TestClass1943:
    def test_solution_0(self, init_variables_1943):
        assert init_variables_1943().splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [
            [1, 4, 14],
            [4, 7, 16],
        ]

    def test_solution_1(self, init_variables_1943):
        assert init_variables_1943().splitPainting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]) == [
            [1, 6, 9],
            [6, 7, 24],
            [7, 8, 15],
            [8, 10, 7],
        ]

    def test_solution_2(self, init_variables_1943):
        assert init_variables_1943().splitPainting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]) == [
            [1, 4, 12],
            [4, 7, 12],
        ]
