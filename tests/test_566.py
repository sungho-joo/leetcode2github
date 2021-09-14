#!/usr/bin/env python

import pytest

"""
Test 566. Reshape the Matrix
"""


@pytest.fixture(scope="session")
def init_variables_566():
    from src.leetcode_566_reshape_the_matrix import Solution

    solution = Solution()

    def _init_variables_566():
        return solution

    yield _init_variables_566


class TestClass566:
    def test_solution_0(self, init_variables_566):
        assert init_variables_566().matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]

    def test_solution_1(self, init_variables_566):
        assert init_variables_566().matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]


#!/usr/bin/env python

import pytest

"""
Test 566. Reshape the Matrix
"""


@pytest.fixture(scope="session")
def init_variables_566():
    from src.leetcode_566_reshape_the_matrix import Solution

    solution = Solution()

    def _init_variables_566():
        return solution

    yield _init_variables_566


class TestClass566:
    def test_solution_0(self, init_variables_566):
        assert init_variables_566().matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]

    def test_solution_1(self, init_variables_566):
        assert init_variables_566().matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
