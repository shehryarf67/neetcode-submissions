class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        path = []

        def backtrack(start, path, total):
            if total == target:
                combinations.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return combinations