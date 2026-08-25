class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start):
            result.append(subset[:])

            for i in range(start, len(nums)):
                # choose
                subset.append(nums[i])

                # explore
                backtrack(i + 1)

                # unchoose
                subset.pop()

        backtrack(0)
        return result