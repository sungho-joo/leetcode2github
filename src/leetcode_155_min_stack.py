# @l2g 155 python3
# [155] Min Stack
# Difficulty: Easy
# https://leetcode.com/problems/min-stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
# Constraints:
#
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
#
#


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            new_min = min(self.stack[-1][1], val)
            self.stack.append([val, new_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_155.py")])
