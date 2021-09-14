#!/usr/bin/env python

import pytest

"""
Test 1889. Minimum Space Wasted From Packaging
"""


@pytest.fixture(scope="session")
def init_variables_1889():
    from src.leetcode_1889_minimum_space_wasted_from_packaging import Solution

    solution = Solution()

    def _init_variables_1889():
        return solution

    yield _init_variables_1889


class TestClass1889:
    def test_solution_0(self, init_variables_1889):
        assert init_variables_1889().minWastedSpace([2, 3, 5], [[4, 8], [2, 8]]) == 6

    def test_solution_1(self, init_variables_1889):
        assert init_variables_1889().minWastedSpace([2, 3, 5], [[1, 4], [2, 3], [3, 4]]) == -1

    def test_solution_2(self, init_variables_1889):
        assert (
            init_variables_1889().minWastedSpace([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]])
            == 9
        )


#!/usr/bin/env python

import pytest

"""
Test 1889. Minimum Space Wasted From Packaging
"""


@pytest.fixture(scope="session")
def init_variables_1889():
    from src.leetcode_1889_minimum_space_wasted_from_packaging import Solution

    solution = Solution()

    def _init_variables_1889():
        return solution

    yield _init_variables_1889


class TestClass1889:
    def test_solution_0(self, init_variables_1889):
        assert init_variables_1889().minWastedSpace([2, 3, 5], [[4, 8], [2, 8]]) == 6

    def test_solution_1(self, init_variables_1889):
        assert init_variables_1889().minWastedSpace([2, 3, 5], [[1, 4], [2, 3], [3, 4]]) == -1

    def test_solution_2(self, init_variables_1889):
        assert (
            init_variables_1889().minWastedSpace([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]])
            == 9
        )
