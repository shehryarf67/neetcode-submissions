class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    number = int(board[i][j])
                    if i not in rows:
                        rows[i] = set()
                    if j not in cols:
                        cols[j] = set()
                    if number in rows[i] or number in cols[j]:
                        return False
                    rows[i].add(number)
                    cols[j].add(number)

                    boxNum = (i // 3) * 3 + (j // 3)
                    if boxNum not in boxes:
                        boxes[boxNum] = set()
                    if number in boxes[boxNum]:
                        return False
                    boxes[boxNum].add(number)

        return True
