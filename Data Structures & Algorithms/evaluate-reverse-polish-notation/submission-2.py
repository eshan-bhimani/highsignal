class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token == '+':
                first = stack.pop()
                second = stack.pop()
                sumT = first + second
                stack.append(sumT)

            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                diff = second - first
                stack.append(diff)

            elif token == '*':
                first = stack.pop()
                second = stack.pop()
                mult = first * second
                stack.append(mult)

            elif token == '/':
                first = stack.pop()
                second = stack.pop()
                quotient = math.floor(second / first)
                stack.append(quotient)
            else:
                stack.append(int(token))

        return stack[-1]