class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if i == ')' and top != '(' or i == '}' and top != '{' or i == ']' and top != '[':
                    return False

        return not stack