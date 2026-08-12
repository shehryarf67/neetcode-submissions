# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    result = ""
    i = 0
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                self.result += "#,"
                return None

            self.result += str(node.val) + ","

            dfs(node.left)
            dfs(node.right) 
        
        dfs(root)
        return self.result

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")

        def dfs():
            if values[self.i] == "#":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
