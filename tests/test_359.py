#!/usr/bin/env python

import pytest

"""
Test 359. Logger Rate Limiter
"""


@pytest.fixture(scope="session")
def init_variables_359():
    from src.leetcode_359_logger_rate_limiter import Solution

    solution = Solution()

    def _init_variables_359():
        return solution

    yield _init_variables_359


class TestClass359:
    def test_solution_0(self, init_variables_359):
        assert (
            init_variables_359().shouldPrintMessage(
                [
                    "Logger",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                ],
                [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]],
            )
            == [None, True, True, False, False, False, True]
        )
