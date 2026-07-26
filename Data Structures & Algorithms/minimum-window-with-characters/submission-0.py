class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = defaultdict(int)

        for c in t:
            count[c] += 1

        left = 0
        needed = len(t)
        minLength = float('inf')
        result = ""

        for right in range(len(s)):
            if count[s[right]] > 0:
                needed -= 1

            count[s[right]] -= 1

            while needed == 0:
                # Add the string to result only if the length is lesser than the current
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    result = s[left:right + 1]

                count[s[left]] += 1
                # Increment the occurrence, if it's non-t, it will always be <= 0
                # So only for t letters it can become > 0
                if count[s[left]] > 0:
                    needed += 1

                left += 1

        return result