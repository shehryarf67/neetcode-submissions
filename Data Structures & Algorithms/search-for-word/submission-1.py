class Solution:
    result = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = ""
        def backtrack(path, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if board[i][j] != word[len(path)]:
                return

            path += board[i][j]

            if path == word:
                self.result = True
                return

            temp = board[i][j]
            board[i][j] = "#"

            backtrack(path, i, j + 1)  # right
            backtrack(path, i, j - 1)  # left
            backtrack(path, i + 1, j)  # down
            backtrack(path, i - 1, j)  # up

            board[i][j] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(path, i, j)

                if self.result:
                    return True

        return False