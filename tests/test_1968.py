#!/usr/bin/env python

import pytest

"""
Test 1968. Array With Elements Not Equal to Average of Neighbors
"""


@pytest.fixture(scope="session")
def init_variables_1968():
    from src.leetcode_1968_array_with_elements_not_equal_to_average_of_neighbors import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1968():
        return solution

    yield _init_variables_1968


class TestClass1968:
    def test_solution_0(self, init_variables_1968):
        assert init_variables_1968().rearrangeArray([1, 2, 3, 4, 5]) == [1, 2, 4, 5, 3]

    def test_solution_1(self, init_variables_1968):
        assert init_variables_1968().rearrangeArray([6, 2, 0, 9, 7]) == [9, 7, 6, 2, 0]


#!/usr/bin/env python

import pytest

"""
Test 1968. Array With Elements Not Equal to Average of Neighbors
"""


@pytest.fixture(scope="session")
def init_variables_1968():
    from src.leetcode_1968_array_with_elements_not_equal_to_average_of_neighbors import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1968():
        return solution

    yield _init_variables_1968


class TestClass1968:
    def test_solution_0(self, init_variables_1968):
        assert init_variables_1968().rearrangeArray([1, 2, 3, 4, 5]) == [1, 2, 4, 5, 3]

    def test_solution_1(self, init_variables_1968):
        assert init_variables_1968().rearrangeArray([6, 2, 0, 9, 7]) == [9, 7, 6, 2, 0]
