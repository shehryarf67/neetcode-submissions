class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = defaultdict(int)

        for c in s1:
            count[c] += 1

        left = 0
        needed = len(s1)

        for right in range(len(s2)):
            if count[s2[right]] > 0:
                needed -= 1

            count[s2[right]] -= 1

            if needed == 0:
                return True

            if right - left + 1 == len(s1):
                if count[s2[left]] >= 0:
                    needed += 1

                count[s2[left]] += 1
                left += 1

        return False