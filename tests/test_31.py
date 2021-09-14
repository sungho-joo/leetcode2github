#!/usr/bin/env python

import pytest

"""
Test 31. Next Permutation
"""


@pytest.fixture(scope="session")
def init_variables_31():
    from src.leetcode_31_next_permutation import Solution

    solution = Solution()

    def _init_variables_31():
        return solution

    yield _init_variables_31


class TestClass31:
    def test_solution_0(self, init_variables_31):
        assert init_variables_31().nextPermutation([1, 2, 3]) == [1, 3, 2]

    def test_solution_1(self, init_variables_31):
        assert init_variables_31().nextPermutation([3, 2, 1]) == [1, 2, 3]

    def test_solution_2(self, init_variables_31):
        assert init_variables_31().nextPermutation([1, 1, 5]) == [1, 5, 1]

    def test_solution_3(self, init_variables_31):
        assert init_variables_31().nextPermutation([1]) == [1]


#!/usr/bin/env python

import pytest

"""
Test 31. Next Permutation
"""


@pytest.fixture(scope="session")
def init_variables_31():
    from src.leetcode_31_next_permutation import Solution

    solution = Solution()

    def _init_variables_31():
        return solution

    yield _init_variables_31


class TestClass31:
    def test_solution_0(self, init_variables_31):
        assert init_variables_31().nextPermutation([1, 2, 3]) == [1, 3, 2]

    def test_solution_1(self, init_variables_31):
        assert init_variables_31().nextPermutation([3, 2, 1]) == [1, 2, 3]

    def test_solution_2(self, init_variables_31):
        assert init_variables_31().nextPermutation([1, 1, 5]) == [1, 5, 1]

    def test_solution_3(self, init_variables_31):
        assert init_variables_31().nextPermutation([1]) == [1]
