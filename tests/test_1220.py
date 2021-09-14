#!/usr/bin/env python

import pytest

"""
Test 1220. Count Vowels Permutation
"""


@pytest.fixture(scope="session")
def init_variables_1220():
    from src.leetcode_1220_count_vowels_permutation import Solution

    solution = Solution()

    def _init_variables_1220():
        return solution

    yield _init_variables_1220


class TestClass1220:
    def test_solution_0(self, init_variables_1220):
        assert init_variables_1220().countVowelPermutation(1) == 5

    def test_solution_1(self, init_variables_1220):
        assert init_variables_1220().countVowelPermutation(2) == 10


#!/usr/bin/env python

import pytest

"""
Test 1220. Count Vowels Permutation
"""


@pytest.fixture(scope="session")
def init_variables_1220():
    from src.leetcode_1220_count_vowels_permutation import Solution

    solution = Solution()

    def _init_variables_1220():
        return solution

    yield _init_variables_1220


class TestClass1220:
    def test_solution_0(self, init_variables_1220):
        assert init_variables_1220().countVowelPermutation(1) == 5

    def test_solution_1(self, init_variables_1220):
        assert init_variables_1220().countVowelPermutation(2) == 10
