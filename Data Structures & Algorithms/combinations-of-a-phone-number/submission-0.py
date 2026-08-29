class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combinations = []
        string = ""

        def backtrack(string, start):
            if len(string) == len(digits):
                combinations.append(string)
                return

            for letter in phone[digits[start]]:
                backtrack(string + letter, start + 1)
            
        backtrack("", 0)
        return combinations