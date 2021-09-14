#!/usr/bin/env python

import pytest

"""
Test 917. Reverse Only Letters
"""


@pytest.fixture(scope="session")
def init_variables_917():
    from src.leetcode_917_reverse_only_letters import Solution

    solution = Solution()

    def _init_variables_917():
        return solution

    yield _init_variables_917


class TestClass917:
    def test_solution_0(self, init_variables_917):
        assert init_variables_917().reverseOnlyLetters("ab-cd") == "dc-ba"

    def test_solution_1(self, init_variables_917):
        assert init_variables_917().reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"

    def test_solution_2(self, init_variables_917):
        assert init_variables_917().reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
