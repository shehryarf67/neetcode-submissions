class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                height = heights[index]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                result = max(result, area)

            stack.append(i)

        while stack:
            index = stack.pop()
            height = heights[index]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            area = height * width
            result = max(result, area)

        return result