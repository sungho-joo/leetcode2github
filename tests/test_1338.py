#!/usr/bin/env python

import pytest

"""
Test 1338. Reduce Array Size to The Half
"""


@pytest.fixture(scope="session")
def init_variables_1338():
    from src.leetcode_1338_reduce_array_size_to_the_half import Solution

    solution = Solution()

    def _init_variables_1338():
        return solution

    yield _init_variables_1338


class TestClass1338:
    def test_solution_0(self, init_variables_1338):
        assert init_variables_1338().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2

    def test_solution_1(self, init_variables_1338):
        assert init_variables_1338().minSetSize([7, 7, 7, 7, 7, 7]) == 1

    def test_solution_2(self, init_variables_1338):
        assert init_variables_1338().minSetSize([1, 9]) == 1

    def test_solution_3(self, init_variables_1338):
        assert init_variables_1338().minSetSize([1000, 1000, 3, 7]) == 1

    def test_solution_4(self, init_variables_1338):
        assert init_variables_1338().minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5


#!/usr/bin/env python

import pytest

"""
Test 1338. Reduce Array Size to The Half
"""


@pytest.fixture(scope="session")
def init_variables_1338():
    from src.leetcode_1338_reduce_array_size_to_the_half import Solution

    solution = Solution()

    def _init_variables_1338():
        return solution

    yield _init_variables_1338


class TestClass1338:
    def test_solution_0(self, init_variables_1338):
        assert init_variables_1338().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2

    def test_solution_1(self, init_variables_1338):
        assert init_variables_1338().minSetSize([7, 7, 7, 7, 7, 7]) == 1

    def test_solution_2(self, init_variables_1338):
        assert init_variables_1338().minSetSize([1, 9]) == 1

    def test_solution_3(self, init_variables_1338):
        assert init_variables_1338().minSetSize([1000, 1000, 3, 7]) == 1

    def test_solution_4(self, init_variables_1338):
        assert init_variables_1338().minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
