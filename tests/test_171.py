#!/usr/bin/env python

import pytest

"""
Test 171. Excel Sheet Column Number
"""


@pytest.fixture(scope="session")
def init_variables_171():
    from src.leetcode_171_excel_sheet_column_number import Solution

    solution = Solution()

    def _init_variables_171():
        return solution

    yield _init_variables_171


class TestClass171:
    def test_solution_0(self, init_variables_171):
        assert init_variables_171().titleToNumber("A") == 1

    def test_solution_1(self, init_variables_171):
        assert init_variables_171().titleToNumber("AB") == 28

    def test_solution_2(self, init_variables_171):
        assert init_variables_171().titleToNumber("ZY") == 701

    def test_solution_3(self, init_variables_171):
        assert init_variables_171().titleToNumber("FXSHRXW") == 2147483647
