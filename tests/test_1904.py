#!/usr/bin/env python

import pytest

"""
Test 1904. The Number of Full Rounds You Have Played
"""


@pytest.fixture(scope="session")
def init_variables_1904():
    from src.leetcode_1904_the_number_of_full_rounds_you_have_played import Solution

    solution = Solution()

    def _init_variables_1904():
        return solution

    yield _init_variables_1904


class TestClass1904:
    def test_solution_0(self, init_variables_1904):
        assert init_variables_1904().numberOfRounds("12:01", "12:44") == 1

    def test_solution_1(self, init_variables_1904):
        assert init_variables_1904().numberOfRounds("20:00", "06:00") == 40

    def test_solution_2(self, init_variables_1904):
        assert init_variables_1904().numberOfRounds("00:00", "23:59") == 95


#!/usr/bin/env python

import pytest

"""
Test 1904. The Number of Full Rounds You Have Played
"""


@pytest.fixture(scope="session")
def init_variables_1904():
    from src.leetcode_1904_the_number_of_full_rounds_you_have_played import Solution

    solution = Solution()

    def _init_variables_1904():
        return solution

    yield _init_variables_1904


class TestClass1904:
    def test_solution_0(self, init_variables_1904):
        assert init_variables_1904().numberOfRounds("12:01", "12:44") == 1

    def test_solution_1(self, init_variables_1904):
        assert init_variables_1904().numberOfRounds("20:00", "06:00") == 40

    def test_solution_2(self, init_variables_1904):
        assert init_variables_1904().numberOfRounds("00:00", "23:59") == 95
