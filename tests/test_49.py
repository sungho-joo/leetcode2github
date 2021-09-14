#!/usr/bin/env python

import pytest

"""
Test 49. Group Anagrams
"""


@pytest.fixture(scope="session")
def init_variables_49():
    from src.leetcode_49_group_anagrams import Solution

    solution = Solution()

    def _init_variables_49():
        return solution

    yield _init_variables_49


class TestClass49:
    def test_solution_0(self, init_variables_49):
        assert init_variables_49().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ]

    def test_solution_1(self, init_variables_49):
        assert init_variables_49().groupAnagrams([""]) == [[""]]

    def test_solution_2(self, init_variables_49):
        assert init_variables_49().groupAnagrams(["a"]) == [["a"]]


#!/usr/bin/env python

import pytest

"""
Test 49. Group Anagrams
"""


@pytest.fixture(scope="session")
def init_variables_49():
    from src.leetcode_49_group_anagrams import Solution

    solution = Solution()

    def _init_variables_49():
        return solution

    yield _init_variables_49


class TestClass49:
    def test_solution_0(self, init_variables_49):
        assert init_variables_49().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ]

    def test_solution_1(self, init_variables_49):
        assert init_variables_49().groupAnagrams([""]) == [[""]]

    def test_solution_2(self, init_variables_49):
        assert init_variables_49().groupAnagrams(["a"]) == [["a"]]
