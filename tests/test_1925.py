#!/usr/bin/env python

import pytest

"""
Test 1925. Count Square Sum Triples
"""


@pytest.fixture(scope="session")
def init_variables_1925():
    from src.leetcode_1925_count_square_sum_triples import Solution

    solution = Solution()

    def _init_variables_1925():
        return solution

    yield _init_variables_1925


class TestClass1925:
    def test_solution_0(self, init_variables_1925):
        assert init_variables_1925().countTriples(5) == 2

    def test_solution_1(self, init_variables_1925):
        assert init_variables_1925().countTriples(10) == 4


#!/usr/bin/env python

import pytest

"""
Test 1925. Count Square Sum Triples
"""


@pytest.fixture(scope="session")
def init_variables_1925():
    from src.leetcode_1925_count_square_sum_triples import Solution

    solution = Solution()

    def _init_variables_1925():
        return solution

    yield _init_variables_1925


class TestClass1925:
    def test_solution_0(self, init_variables_1925):
        assert init_variables_1925().countTriples(5) == 2

    def test_solution_1(self, init_variables_1925):
        assert init_variables_1925().countTriples(10) == 4
