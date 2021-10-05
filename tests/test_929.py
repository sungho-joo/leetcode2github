#!/usr/bin/env python

import pytest

"""
Test 929. Unique Email Addresses
"""


@pytest.fixture(scope="session")
def init_variables_929():
    from src.leetcode_929_unique_email_addresses import Solution

    solution = Solution()

    def _init_variables_929():
        return solution

    yield _init_variables_929


class TestClass929:
    def test_solution_0(self, init_variables_929):
        assert (
            init_variables_929().numUniqueEmails(
                [
                    "test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com",
                ]
            )
            == 2
        )

    def test_solution_1(self, init_variables_929):
        assert (
            init_variables_929().numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])
            == 3
        )
