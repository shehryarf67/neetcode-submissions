# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            # Both left and right subtrees must match
            return (sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right))

        # An empty subRoot is considered a subtree
        if not subRoot:
            return True

        # A non-empty subRoot cannot exist inside an empty root
        if not root:
            return False

        # Try matching subRoot starting at the current root node
        if sameTree(root, subRoot):
            return True

        # Otherwise search in root's left and right subtrees
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))