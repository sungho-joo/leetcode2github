#!/usr/bin/env python

import pytest

"""
Test 838. Push Dominoes
"""


@pytest.fixture(scope="session")
def init_variables_838():
    from src.leetcode_838_push_dominoes import Solution

    solution = Solution()

    def _init_variables_838():
        return solution

    yield _init_variables_838


class TestClass838:
    def test_solution_0(self, init_variables_838):
        assert init_variables_838().pushDominoes("RR.L") == "RR.L"

    def test_solution_1(self, init_variables_838):
        assert init_variables_838().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."


#!/usr/bin/env python

import pytest

"""
Test 838. Push Dominoes
"""


@pytest.fixture(scope="session")
def init_variables_838():
    from src.leetcode_838_push_dominoes import Solution

    solution = Solution()

    def _init_variables_838():
        return solution

    yield _init_variables_838


class TestClass838:
    def test_solution_0(self, init_variables_838):
        assert init_variables_838().pushDominoes("RR.L") == "RR.L"

    def test_solution_1(self, init_variables_838):
        assert init_variables_838().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
