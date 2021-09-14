#!/usr/bin/env python

import pytest

"""
Test 1825. Finding MK Average
"""


@pytest.fixture(scope="session")
def init_variables_1825():
    from src.leetcode_1825_finding_mk_average import MKAverage

    solution = MKAverage(3, 1)

    def _init_variables_1825():
        return solution

    yield _init_variables_1825


class TestClass1825:
    def test_solution_0(self, init_variables_1825):
        assert init_variables_1825().addElement(3) == None
        assert init_variables_1825().addElement(1) == None
        assert init_variables_1825().calculateMKAverage() == -1
        assert init_variables_1825().addElement(10) == None
        assert init_variables_1825().calculateMKAverage() == 3
        assert init_variables_1825().addElement(5) == None
        assert init_variables_1825().addElement(5) == None
        assert init_variables_1825().addElement(5) == None
        assert init_variables_1825().calculateMKAverage() == 5
