#!/usr/bin/env python

import pytest

"""
Test 40. Combination Sum II
"""


@pytest.fixture(scope="session")
def init_variables_40():
    from src.leetcode_40_combination_sum_ii import Solution
    solution = Solution()

    def _init_variables_40():
        return solution

    yield _init_variables_40

class TestClass40:
    def test_solution_0(self, init_variables_40):
        assert init_variables_40().                            combinationSum2([10,1,2,7,6,1,5], 8) == 

    def test_solution_1(self, init_variables_40):
        assert init_variables_40().                            combinationSum2([2,5,2,1,2], 5) == 
#!/usr/bin/env python

import pytest

"""
Test 40. Combination Sum II
"""


@pytest.fixture(scope="session")
def init_variables_40():
    from src.leetcode_40_combination_sum_ii import Solution
    solution = Solution()

    def _init_variables_40():
        return solution

    yield _init_variables_40

class TestClass40:
    def test_solution_0(self, init_variables_40):
        assert init_variables_40().                            combinationSum2([10,1,2,7,6,1,5], 8) == 

    def test_solution_1(self, init_variables_40):
        assert init_variables_40().                            combinationSum2([2,5,2,1,2], 5) == 
