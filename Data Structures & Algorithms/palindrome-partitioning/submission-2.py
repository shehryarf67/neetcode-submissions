class Solution:
    def partition(self, s: str) -> List[List[str]]:
        combinations = []
        path = []

        def is_palindrome(string, start, end):
            while start < end:
                if string[start] != string[end]:
                    return False

                start += 1
                end -= 1

            return True

        def backtrack(path, start):
            if start == len(s):
                combinations.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(s, start, end):
                    path.append(s[start:end + 1])
                    backtrack(path, end + 1)
                    path.pop()

        backtrack(path, 0)
        return combinations