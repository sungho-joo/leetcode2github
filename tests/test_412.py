#!/usr/bin/env python

import pytest

"""
Test 412. Fizz Buzz
"""


@pytest.fixture(scope="session")
def init_variables_412():
    from src.leetcode_412_fizz_buzz import Solution

    solution = Solution()

    def _init_variables_412():
        return solution

    yield _init_variables_412


class TestClass412:
    def test_solution_0(self, init_variables_412):
        assert init_variables_412().fizzBuzz(3) == ["1", "2", "Fizz"]

    def test_solution_1(self, init_variables_412):
        assert init_variables_412().fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_solution_2(self, init_variables_412):
        assert init_variables_412().fizzBuzz(15) == [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
