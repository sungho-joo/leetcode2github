#!/usr/bin/env python

import pytest

"""
Test 1865. Finding Pairs With a Certain Sum
"""


@pytest.fixture(scope="session")
def init_variables_1865():
    from src.leetcode_1865_finding_pairs_with_a_certain_sum import FindSumPairs

    solution = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

    def _init_variables_1865():
        return solution

    yield _init_variables_1865


class TestClass1865:
    def test_solution_0(self, init_variables_1865):
        assert init_variables_1865().count(7) == 8
        assert init_variables_1865().add(3, 2) == None
        assert init_variables_1865().count(8) == 2
        assert init_variables_1865().count(4) == 1
        assert init_variables_1865().add(0, 1) == None
        assert init_variables_1865().add(1, 1) == None
        assert init_variables_1865().count(7) == 11


#!/usr/bin/env python

import pytest

"""
Test 1865. Finding Pairs With a Certain Sum
"""


@pytest.fixture(scope="session")
def init_variables_1865():
    from src.leetcode_1865_finding_pairs_with_a_certain_sum import FindSumPairs

    solution = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

    def _init_variables_1865():
        return solution

    yield _init_variables_1865


class TestClass1865:
    def test_solution_0(self, init_variables_1865):
        assert init_variables_1865().count(7) == 8
        assert init_variables_1865().add(3, 2) == None
        assert init_variables_1865().count(8) == 2
        assert init_variables_1865().count(4) == 1
        assert init_variables_1865().add(0, 1) == None
        assert init_variables_1865().add(1, 1) == None
        assert init_variables_1865().count(7) == 11
