class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return

        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        
        index = {}
        for i, num in enumerate(nums):
            index[num] = i

        uf = UnionFind(len(nums))

        for num in nums:
            if num + 1 in index:
                uf.union(index[num], index[num + 1])
        
        longest = 1
        for i in range(len(nums)):
            root = uf.find(i)
            longest = max(longest, uf.size[root])

        return longest