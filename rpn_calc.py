import operator
from typing import *
import re

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def div(l, r) -> int:
            return int(l / r)

        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": div}

        num_stack = []
        for tok in tokens:
            if re.match(r'[+\-]?\d+$', tok):
                num_stack.append(int(tok))
            else:
                r = num_stack.pop()
                l = num_stack.pop()
                num = ops[tok](l, r)
                print(f'{tok}({l}, {r}) = {num}')
                num_stack.append(num)
        return num_stack[-1]


if __name__ == '__main__':
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
