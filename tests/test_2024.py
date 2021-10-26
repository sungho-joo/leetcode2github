#!/usr/bin/env python

import pytest

"""
Test 2024. Maximize the Confusion of an Exam
"""


@pytest.fixture(scope="session")
def init_variables_2024():
    from src.leetcode_2024_maximize_the_confusion_of_an_exam import Solution

    solution = Solution()

    def _init_variables_2024():
        return solution

    yield _init_variables_2024


class TestClass2024:
    def test_solution_0(self, init_variables_2024):
        assert init_variables_2024().maxConsecutiveAnswers("TTFF", 2) == 4

    def test_solution_1(self, init_variables_2024):
        assert init_variables_2024().maxConsecutiveAnswers("TFFT", 1) == 3

    def test_solution_2(self, init_variables_2024):
        assert init_variables_2024().maxConsecutiveAnswers("TTFTTFTT", 1) == 5
