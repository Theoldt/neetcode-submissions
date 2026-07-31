class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            seen_col = {}
            seen_row = {}
            for j in range(len(board[i])):
                if board[i][j] != "." and board[i][j] in seen_row:
                    return False
                elif board[i][j] != ".":
                    seen_row[board[i][j]] = True

                if board[j][i] != "." and board[j][i] in seen_col:
                    return False
                elif board[j][i] != ".":
                    seen_col[board[j][i]] = True

        
        start_box = []

        for i in range(len(board)):
            for j in range(len(board)):
                if i % 3 == 0 and j % 3 == 0:
                    start_box.append((i,j))


        for start_row, start_col in start_box:
            box = {}
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] != "." and board[i][j] in box:
                        return False
                    elif board[i][j] != ".":
                        box[board[i][j]] = True

        return True
                


