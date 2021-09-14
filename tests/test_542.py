#!/usr/bin/env python

import pytest

"""
Test 542. 01 Matrix
"""


@pytest.fixture(scope="session")
def init_variables_542():
    from src.leetcode_542_01_matrix import Solution

    solution = Solution()

    def _init_variables_542():
        return solution

    yield _init_variables_542


class TestClass542:
    def test_solution_0(self, init_variables_542):
        assert init_variables_542().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]

    def test_solution_1(self, init_variables_542):
        assert init_variables_542().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1],
        ]


#!/usr/bin/env python

import pytest

"""
Test 542. 01 Matrix
"""


@pytest.fixture(scope="session")
def init_variables_542():
    from src.leetcode_542_01_matrix import Solution

    solution = Solution()

    def _init_variables_542():
        return solution

    yield _init_variables_542


class TestClass542:
    def test_solution_0(self, init_variables_542):
        assert init_variables_542().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]

    def test_solution_1(self, init_variables_542):
        assert init_variables_542().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1],
        ]
