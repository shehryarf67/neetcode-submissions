# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_sum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            # Get the best contribution from each child.
            # If a branch contributes negatively, ignore it.
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best complete path that passes THROUGH this node.
            # This path is allowed to use both children.
            current_path = node.val + left + right

            # See if this is the best path we've found anywhere.
            self.max_sum = max(self.max_sum, current_path)

            # When returning upward, we can only choose ONE child
            # so that the path doesn't branch.
            return node.val + max(left, right)

        dfs(root)

        return self.max_sum