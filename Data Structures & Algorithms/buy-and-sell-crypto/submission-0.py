class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        lowest = float("inf")

        for price in prices:
            if price < lowest:
                lowest = price
            temp = price - lowest
            if temp > highest:
                highest = temp

        return highest