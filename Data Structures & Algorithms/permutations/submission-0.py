class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        path = []

        def backtrack(start, path, length):
            if length == len(nums):
                combinations.append(path[:])
                return 

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i + 1, path, len(path))
                    path.pop()

        backtrack(0, [], 0)
        return combinations