#!/usr/bin/env python

import pytest

"""
Test 26. Remove Duplicates from Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_26():
    from src.leetcode_26_remove_duplicates_from_sorted_array import Solution
    solution = Solution()

    def _init_variables_26():
        return solution

    yield _init_variables_26

class TestClass26:
    def test_solution_0(self, init_variables_26):
        assert init_variables_26().                            removeDuplicates([1,1,2]) == 2, nums = [1,2,_]

    def test_solution_1(self, init_variables_26):
        assert init_variables_26().                            removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5, nums = [0,1,2,3,4,_,_,_,_,_]
#!/usr/bin/env python

import pytest

"""
Test 26. Remove Duplicates from Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_26():
    from src.leetcode_26_remove_duplicates_from_sorted_array import Solution
    solution = Solution()

    def _init_variables_26():
        return solution

    yield _init_variables_26

class TestClass26:
    def test_solution_0(self, init_variables_26):
        assert init_variables_26().                            removeDuplicates([1,1,2]) == 2, nums = [1,2,_]

    def test_solution_1(self, init_variables_26):
        assert init_variables_26().                            removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5, nums = [0,1,2,3,4,_,_,_,_,_]
