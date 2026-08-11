# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    pre_index = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # value -> index in inorder
        inorder_index = {}

        for i, val in enumerate(inorder):
            inorder_index[val] = i


        def build(left, right):
            # No nodes in this inorder range
            if left > right:
                return None

            # Preorder gives us the next root
            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            # Find root's position in inorder in O(1)
            mid = inorder_index[root_val]

            # Build left subtree first because preorder is:
            # Root -> Left -> Right
            root.left = build(left, mid - 1)

            # Then build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)