class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        answer = j

        while i <= j:
            k = (i + j) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                answer = k
                j = k - 1
            else:
                i = k + 1

        return answer