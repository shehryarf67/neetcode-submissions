class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        string = ""

        def backtrack(string, forwardBrack, backwardBrack):
            if len(string) == n * 2:
                combinations.append(string)
                return

            if forwardBrack < n:
                backtrack(string + "(", forwardBrack + 1, backwardBrack)

            if backwardBrack < forwardBrack:
                backtrack(string + ")", forwardBrack, backwardBrack + 1)

        backtrack(string, 0, 0)
        return combinations