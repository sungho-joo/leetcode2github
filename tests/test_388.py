#!/usr/bin/env python

import pytest

"""
Test 388. Longest Absolute File Path
"""


@pytest.fixture(scope="session")
def init_variables_388():
    from src.leetcode_388_longest_absolute_file_path import Solution

    solution = Solution()

    def _init_variables_388():
        return solution

    yield _init_variables_388


class TestClass388:
    def test_solution_0(self, init_variables_388):
        assert init_variables_388().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20

    def test_solution_1(self, init_variables_388):
        assert (
            init_variables_388().lengthLongestPath(
                "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
            )
            == 32
        )

    def test_solution_2(self, init_variables_388):
        assert init_variables_388().lengthLongestPath("a") == 0

    def test_solution_3(self, init_variables_388):
        assert init_variables_388().lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt") == 12
