#!/usr/bin/env python

import pytest

"""
Test 1944. Number of Visible People in a Queue
"""


@pytest.fixture(scope="session")
def init_variables_1944():
    from src.leetcode_1944_number_of_visible_people_in_a_queue import Solution

    solution = Solution()

    def _init_variables_1944():
        return solution

    yield _init_variables_1944


class TestClass1944:
    def test_solution_0(self, init_variables_1944):
        assert init_variables_1944().canSeePersonsCount([10, 6, 8, 5, 11, 9]) == [3, 1, 2, 1, 1, 0]

    def test_solution_1(self, init_variables_1944):
        assert init_variables_1944().canSeePersonsCount([5, 1, 2, 3, 10]) == [4, 1, 1, 1, 0]


#!/usr/bin/env python

import pytest

"""
Test 1944. Number of Visible People in a Queue
"""


@pytest.fixture(scope="session")
def init_variables_1944():
    from src.leetcode_1944_number_of_visible_people_in_a_queue import Solution

    solution = Solution()

    def _init_variables_1944():
        return solution

    yield _init_variables_1944


class TestClass1944:
    def test_solution_0(self, init_variables_1944):
        assert init_variables_1944().canSeePersonsCount([10, 6, 8, 5, 11, 9]) == [3, 1, 2, 1, 1, 0]

    def test_solution_1(self, init_variables_1944):
        assert init_variables_1944().canSeePersonsCount([5, 1, 2, 3, 10]) == [4, 1, 1, 1, 0]
