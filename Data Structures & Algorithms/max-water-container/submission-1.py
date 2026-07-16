class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index1 = 0
        index2 = len(heights) - 1
        area = 0

        while index1 < index2:
            tempArea = min(heights[index1], heights[index2]) * (index2 - index1)
            if tempArea > area:
                area = tempArea
            if heights[index1] > heights[index2]:
                index2 -= 1
            else:
                index1 += 1
        
        return area