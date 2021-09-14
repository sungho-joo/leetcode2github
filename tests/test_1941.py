#!/usr/bin/env python

import pytest

"""
Test 1941. Check if All Characters Have Equal Number of Occurrences
"""


@pytest.fixture(scope="session")
def init_variables_1941():
    from src.leetcode_1941_check_if_all_characters_have_equal_number_of_occurrences import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1941():
        return solution

    yield _init_variables_1941


class TestClass1941:
    def test_solution_0(self, init_variables_1941):
        assert init_variables_1941().areOccurrencesEqual("abacbc")

    def test_solution_1(self, init_variables_1941):
        assert not init_variables_1941().areOccurrencesEqual("aaabb")


#!/usr/bin/env python

import pytest

"""
Test 1941. Check if All Characters Have Equal Number of Occurrences
"""


@pytest.fixture(scope="session")
def init_variables_1941():
    from src.leetcode_1941_check_if_all_characters_have_equal_number_of_occurrences import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1941():
        return solution

    yield _init_variables_1941


class TestClass1941:
    def test_solution_0(self, init_variables_1941):
        assert init_variables_1941().areOccurrencesEqual("abacbc")

    def test_solution_1(self, init_variables_1941):
        assert not init_variables_1941().areOccurrencesEqual("aaabb")
