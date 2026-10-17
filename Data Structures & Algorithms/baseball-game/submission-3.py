class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        for op in operations:
            if op == '+':
                new_score = int(stack[-1]) + int(stack[-2])
                stack.append(new_score)
            elif op == 'D':
                new_score = int(stack[-1]) * 2
                stack.append(new_score)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

                


        