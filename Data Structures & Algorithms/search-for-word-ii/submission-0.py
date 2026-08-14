class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build Trie
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            # Marks the end of a complete word
            node.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # 2. DFS / Backtracking
        def dfs(row, col, node):

            # Out of bounds or already visited
            if (row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == "#"):
                return

            char = board[row][col]

            # Trie pruning:
            # No word starts with our current path
            if char not in node.children:
                return

            # Move down the Trie
            node = node.children[char]

            # Found a complete word
            if node.word is not None:
                result.append(node.word)

                # Prevent duplicate results
                node.word = None

            # Mark cell as visited
            board[row][col] = "#"

            # Explore all 4 directions
            dfs(row + 1, col, node)  # down
            dfs(row - 1, col, node)  # up
            dfs(row, col + 1, node)  # right
            dfs(row, col - 1, node)  # left

            # Backtrack
            board[row][col] = char

        # 3. Try starting from every board position
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result