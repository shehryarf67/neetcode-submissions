class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        maxLen = 0
        left = 0

        for right in range(len(s)):
            if s[right] in lastSeen and lastSeen[s[right]] >= left:
                left = lastSeen[s[right]] + 1

            lastSeen[s[right]] = right
            maxLen = max(maxLen, right-left+1)

        return maxLen
        