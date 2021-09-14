#!/usr/bin/env python

import pytest

"""
Test 205. Isomorphic Strings
"""


@pytest.fixture(scope="session")
def init_variables_205():
    from src.leetcode_205_isomorphic_strings import Solution

    solution = Solution()

    def _init_variables_205():
        return solution

    yield _init_variables_205


class TestClass205:
    def test_solution_0(self, init_variables_205):
        assert init_variables_205().isIsomorphic("egg", "add")

    def test_solution_1(self, init_variables_205):
        assert not init_variables_205().isIsomorphic("foo", "bar")

    def test_solution_2(self, init_variables_205):
        assert init_variables_205().isIsomorphic("paper", "title")


#!/usr/bin/env python

import pytest

"""
Test 205. Isomorphic Strings
"""


@pytest.fixture(scope="session")
def init_variables_205():
    from src.leetcode_205_isomorphic_strings import Solution

    solution = Solution()

    def _init_variables_205():
        return solution

    yield _init_variables_205


class TestClass205:
    def test_solution_0(self, init_variables_205):
        assert init_variables_205().isIsomorphic("egg", "add")

    def test_solution_1(self, init_variables_205):
        assert not init_variables_205().isIsomorphic("foo", "bar")

    def test_solution_2(self, init_variables_205):
        assert init_variables_205().isIsomorphic("paper", "title")
