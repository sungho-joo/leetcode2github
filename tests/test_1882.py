#!/usr/bin/env python

import pytest

"""
Test 1882. Process Tasks Using Servers
"""


@pytest.fixture(scope="session")
def init_variables_1882():
    from src.leetcode_1882_process_tasks_using_servers import Solution

    solution = Solution()

    def _init_variables_1882():
        return solution

    yield _init_variables_1882


class TestClass1882:
    def test_solution_0(self, init_variables_1882):
        assert init_variables_1882().assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]

    def test_solution_1(self, init_variables_1882):
        assert init_variables_1882().assignTasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]) == [
            1,
            4,
            1,
            4,
            1,
            3,
            2,
        ]


#!/usr/bin/env python

import pytest

"""
Test 1882. Process Tasks Using Servers
"""


@pytest.fixture(scope="session")
def init_variables_1882():
    from src.leetcode_1882_process_tasks_using_servers import Solution

    solution = Solution()

    def _init_variables_1882():
        return solution

    yield _init_variables_1882


class TestClass1882:
    def test_solution_0(self, init_variables_1882):
        assert init_variables_1882().assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]

    def test_solution_1(self, init_variables_1882):
        assert init_variables_1882().assignTasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]) == [
            1,
            4,
            1,
            4,
            1,
            3,
            2,
        ]
