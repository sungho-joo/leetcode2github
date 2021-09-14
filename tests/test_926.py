#!/usr/bin/env python

import pytest

"""
Test 926. Flip String to Monotone Increasing
"""


@pytest.fixture(scope="session")
def init_variables_926():
    from src.leetcode_926_flip_string_to_monotone_increasing import Solution

    solution = Solution()

    def _init_variables_926():
        return solution

    yield _init_variables_926


class TestClass926:
    def test_solution_0(self, init_variables_926):
        assert init_variables_926().minFlipsMonoIncr("00110") == 1

    def test_solution_1(self, init_variables_926):
        assert init_variables_926().minFlipsMonoIncr("010110") == 2

    def test_solution_2(self, init_variables_926):
        assert init_variables_926().minFlipsMonoIncr("00011000") == 2


#!/usr/bin/env python

import pytest

"""
Test 926. Flip String to Monotone Increasing
"""


@pytest.fixture(scope="session")
def init_variables_926():
    from src.leetcode_926_flip_string_to_monotone_increasing import Solution

    solution = Solution()

    def _init_variables_926():
        return solution

    yield _init_variables_926


class TestClass926:
    def test_solution_0(self, init_variables_926):
        assert init_variables_926().minFlipsMonoIncr("00110") == 1

    def test_solution_1(self, init_variables_926):
        assert init_variables_926().minFlipsMonoIncr("010110") == 2

    def test_solution_2(self, init_variables_926):
        assert init_variables_926().minFlipsMonoIncr("00011000") == 2
