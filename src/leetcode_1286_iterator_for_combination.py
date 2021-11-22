# @l2g 1286 python3
# [1286] Iterator for Combination
# Difficulty: Medium
# https://leetcode.com/problems/iterator-for-combination
#
# Design the CombinationIterator class:
#
# CombinationIterator(string characters,
# int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.
#
#
# Example 1:
#
# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]
#
# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False
#
#
# Constraints:
#
# 1 <= combinationLength <= characters.length <= 15
# All the characters of characters are unique.
# At most 10^4 calls will be made to next and hasNext.
# It is guaranteed that all calls of the function next are valid.
#
#


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.k = combinationLength
        self.combinations = []
        self.get_combinations(0, [])
        self.idx = 0

    def get_combinations(self, pos, arr):
        if len(arr) == self.k:
            self.combinations.append("".join(arr))
            return

        for next_pos in range(pos, len(self.characters)):
            self.get_combinations(next_pos + 1, arr + [self.characters[next_pos]])

    def next(self) -> str:
        ans = self.combinations[self.idx]
        self.idx += 1
        return ans

    def hasNext(self) -> bool:
        return self.idx < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1286.py")])
