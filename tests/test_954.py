#!/usr/bin/env python

import pytest

"""
Test 954. Array of Doubled Pairs
"""


@pytest.fixture(scope="session")
def init_variables_954():
    from src.leetcode_954_array_of_doubled_pairs import Solution

    solution = Solution()

    def _init_variables_954():
        return solution

    yield _init_variables_954


class TestClass954:
    def test_solution_0(self, init_variables_954):
        assert not init_variables_954().canReorderDoubled([3, 1, 3, 6])

    def test_solution_1(self, init_variables_954):
        assert not init_variables_954().canReorderDoubled([2, 1, 2, 6])

    def test_solution_2(self, init_variables_954):
        assert init_variables_954().canReorderDoubled([4, -2, 2, -4])

    def test_solution_3(self, init_variables_954):
        assert not init_variables_954().canReorderDoubled([1, 2, 4, 16, 8, 4])


#!/usr/bin/env python

import pytest

"""
Test 954. Array of Doubled Pairs
"""


@pytest.fixture(scope="session")
def init_variables_954():
    from src.leetcode_954_array_of_doubled_pairs import Solution

    solution = Solution()

    def _init_variables_954():
        return solution

    yield _init_variables_954


class TestClass954:
    def test_solution_0(self, init_variables_954):
        assert not init_variables_954().canReorderDoubled([3, 1, 3, 6])

    def test_solution_1(self, init_variables_954):
        assert not init_variables_954().canReorderDoubled([2, 1, 2, 6])

    def test_solution_2(self, init_variables_954):
        assert init_variables_954().canReorderDoubled([4, -2, 2, -4])

    def test_solution_3(self, init_variables_954):
        assert not init_variables_954().canReorderDoubled([1, 2, 4, 16, 8, 4])
