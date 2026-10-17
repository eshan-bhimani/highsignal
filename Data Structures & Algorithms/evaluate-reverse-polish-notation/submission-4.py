class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for token in tokens:

            if token == '+':
                one = stack.pop()
                two = stack.pop()
                sumT = one + two
                stack.append(sumT)

            elif token == '-':
                one = stack.pop()
                two = stack.pop()
                diff = two - one
                stack.append(diff)

            elif token == '*':
                one = stack.pop()
                two = stack.pop()
                mult = one * two
                stack.append(mult)

            elif token == '/':
                one = stack.pop()
                two = stack.pop()
                quotient = int(two/one)
                stack.append(quotient)

            else:
                stack.append(int(token))

        return stack[-1]
        