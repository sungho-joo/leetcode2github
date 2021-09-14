#!/usr/bin/env python

import pytest

"""
Test 718. Maximum Length of Repeated Subarray
"""


@pytest.fixture(scope="session")
def init_variables_718():
    from src.leetcode_718_maximum_length_of_repeated_subarray import Solution

    solution = Solution()

    def _init_variables_718():
        return solution

    yield _init_variables_718


class TestClass718:
    def test_solution_0(self, init_variables_718):
        assert init_variables_718().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3

    def test_solution_1(self, init_variables_718):
        assert init_variables_718().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5


#!/usr/bin/env python

import pytest

"""
Test 718. Maximum Length of Repeated Subarray
"""


@pytest.fixture(scope="session")
def init_variables_718():
    from src.leetcode_718_maximum_length_of_repeated_subarray import Solution

    solution = Solution()

    def _init_variables_718():
        return solution

    yield _init_variables_718


class TestClass718:
    def test_solution_0(self, init_variables_718):
        assert init_variables_718().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3

    def test_solution_1(self, init_variables_718):
        assert init_variables_718().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5
