class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # 2-step jump
            if slow == fast:
                break

        # Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow