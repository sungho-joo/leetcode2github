#!/usr/bin/env python

import pytest

"""
Test 91. Decode Ways
"""


@pytest.fixture(scope="session")
def init_variables_91():
    from src.leetcode_91_decode_ways import Solution

    solution = Solution()

    def _init_variables_91():
        return solution

    yield _init_variables_91


class TestClass91:
    def test_solution_0(self, init_variables_91):
        assert init_variables_91().numDecodings("12") == 2

    def test_solution_1(self, init_variables_91):
        assert init_variables_91().numDecodings("226") == 3

    def test_solution_2(self, init_variables_91):
        assert init_variables_91().numDecodings("0") == 0

    def test_solution_3(self, init_variables_91):
        assert init_variables_91().numDecodings("06") == 0


#!/usr/bin/env python

import pytest

"""
Test 91. Decode Ways
"""


@pytest.fixture(scope="session")
def init_variables_91():
    from src.leetcode_91_decode_ways import Solution

    solution = Solution()

    def _init_variables_91():
        return solution

    yield _init_variables_91


class TestClass91:
    def test_solution_0(self, init_variables_91):
        assert init_variables_91().numDecodings("12") == 2

    def test_solution_1(self, init_variables_91):
        assert init_variables_91().numDecodings("226") == 3

    def test_solution_2(self, init_variables_91):
        assert init_variables_91().numDecodings("0") == 0

    def test_solution_3(self, init_variables_91):
        assert init_variables_91().numDecodings("06") == 0
