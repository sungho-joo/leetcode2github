#!/usr/bin/env python

import pytest

"""
Test 208. Implement Trie (Prefix Tree)
"""


@pytest.fixture(scope="session")
def init_variables_208():
    from src.leetcode_208_implement_trie_prefix_tree import insert

    solution = insert()

    def _init_variables_208():
        return solution

    yield _init_variables_208


class TestClass208:
    def test_solution_0(self, init_variables_208):
        assert init_variables_208().insert("apple") == None
        assert init_variables_208().search("apple") == True
        assert init_variables_208().search("app") == False
        assert init_variables_208().startsWith("app") == True
        assert init_variables_208().insert("app") == None
        assert init_variables_208().search("app") == True
