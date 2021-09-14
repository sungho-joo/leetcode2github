#!/usr/bin/env python

import pytest

"""
Test 1952. Three Divisors
"""


@pytest.fixture(scope="session")
def init_variables_1952():
    from src.leetcode_1952_three_divisors import Solution

    solution = Solution()

    def _init_variables_1952():
        return solution

    yield _init_variables_1952


class TestClass1952:
    def test_solution_0(self, init_variables_1952):
        assert not init_variables_1952().isThree(2)

    def test_solution_1(self, init_variables_1952):
        assert init_variables_1952().isThree(4)


#!/usr/bin/env python

import pytest

"""
Test 1952. Three Divisors
"""


@pytest.fixture(scope="session")
def init_variables_1952():
    from src.leetcode_1952_three_divisors import Solution

    solution = Solution()

    def _init_variables_1952():
        return solution

    yield _init_variables_1952


class TestClass1952:
    def test_solution_0(self, init_variables_1952):
        assert not init_variables_1952().isThree(2)

    def test_solution_1(self, init_variables_1952):
        assert init_variables_1952().isThree(4)
