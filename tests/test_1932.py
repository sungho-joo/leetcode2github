#!/usr/bin/env python

import pytest

"""
Test 1932. Merge BSTs to Create Single BST
"""


@pytest.fixture(scope="session")
def init_variables_1932():
    from src.leetcode_1932_merge_bsts_to_create_single_bst import Solution

    solution = Solution()

    def _init_variables_1932():
        return solution

    yield _init_variables_1932


class TestClass1932:
    def test_solution_0(self, init_variables_1932):
        assert init_variables_1932().canMerge([[2, 1], [3, 2, 5], [5, 4]]) == [3, 2, 5, 1, None, 4]

    def test_solution_1(self, init_variables_1932):
        assert init_variables_1932().canMerge([[5, 3, 8], [3, 2, 6]]) == []

    def test_solution_2(self, init_variables_1932):
        assert init_variables_1932().canMerge([[5, 4], [3]]) == []

    def test_solution_3(self, init_variables_1932):
        assert init_variables_1932().canMerge([[2, 1, 3]]) == [2, 1, 3]


#!/usr/bin/env python

import pytest

"""
Test 1932. Merge BSTs to Create Single BST
"""


@pytest.fixture(scope="session")
def init_variables_1932():
    from src.leetcode_1932_merge_bsts_to_create_single_bst import Solution

    solution = Solution()

    def _init_variables_1932():
        return solution

    yield _init_variables_1932


class TestClass1932:
    def test_solution_0(self, init_variables_1932):
        assert init_variables_1932().canMerge([[2, 1], [3, 2, 5], [5, 4]]) == [3, 2, 5, 1, None, 4]

    def test_solution_1(self, init_variables_1932):
        assert init_variables_1932().canMerge([[5, 3, 8], [3, 2, 6]]) == []

    def test_solution_2(self, init_variables_1932):
        assert init_variables_1932().canMerge([[5, 4], [3]]) == []

    def test_solution_3(self, init_variables_1932):
        assert init_variables_1932().canMerge([[2, 1, 3]]) == [2, 1, 3]
