#!/usr/bin/env python

import pytest

"""
Test 1974. Minimum Time to Type Word Using Special Typewriter
"""


@pytest.fixture(scope="session")
def init_variables_1974():
    from src.leetcode_1974_minimum_time_to_type_word_using_special_typewriter import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1974():
        return solution

    yield _init_variables_1974


class TestClass1974:
    def test_solution_0(self, init_variables_1974):
        assert init_variables_1974().minTimeToType("abc") == 5

    def test_solution_1(self, init_variables_1974):
        assert init_variables_1974().minTimeToType("bza") == 7

    def test_solution_2(self, init_variables_1974):
        assert init_variables_1974().minTimeToType("zjpc") == 34
