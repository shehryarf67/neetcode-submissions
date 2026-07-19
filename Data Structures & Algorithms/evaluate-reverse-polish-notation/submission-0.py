class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = 0

        for token in tokens:
            if token == '/' or token == '*' or token == '+' or token == '-':
                value1 = int(stack.pop())
                value2 = int(stack.pop())

                if token == '/':
                    value = int(float(value2) / value1)
                    print(value)
                elif token == '-':
                    value = value2 - value1
                elif token == '*':
                    value = value1 * value2
                elif token == '+':
                    value = value1 + value2
                stack.append(value)
            else:
                stack.append(token)

        return int(stack.pop())