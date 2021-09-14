#!/usr/bin/env python

import pytest

"""
Test 791. Custom Sort String
"""


@pytest.fixture(scope="session")
def init_variables_791():
    from src.leetcode_791_custom_sort_string import Solution

    solution = Solution()

    def _init_variables_791():
        return solution

    yield _init_variables_791


class TestClass791:
    def test_solution_0(self, init_variables_791):
        assert init_variables_791().customSortString("cba", "abcd") == "cbad"

    def test_solution_1(self, init_variables_791):
        assert init_variables_791().customSortString("cbafg", "abcd") == "cbad"


#!/usr/bin/env python

import pytest

"""
Test 791. Custom Sort String
"""


@pytest.fixture(scope="session")
def init_variables_791():
    from src.leetcode_791_custom_sort_string import Solution

    solution = Solution()

    def _init_variables_791():
        return solution

    yield _init_variables_791


class TestClass791:
    def test_solution_0(self, init_variables_791):
        assert init_variables_791().customSortString("cba", "abcd") == "cbad"

    def test_solution_1(self, init_variables_791):
        assert init_variables_791().customSortString("cbafg", "abcd") == "cbad"
