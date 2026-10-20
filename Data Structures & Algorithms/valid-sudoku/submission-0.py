class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_box(row, col) :
            seen = set()
            for i in range(row, row+3) :
                for j in range(col, col+3) :
                    if board[i][j] == "." :
                        continue
                    if board[i][j] in seen :
                        return False
                    else :
                        seen.add(board[i][j])
            return True
        
        for j in range(9) :
            seen = set()
            for i in range(9) :
                if board[i][j] == "." :
                    continue
                if board[i][j] in seen :
                    print("failed at col check")
                    return False
                else :
                    seen.add(board[i][j])
        
        for i in range(9) :
            seen = set()
            for j in range(9) :
                if board[i][j] == "." :
                    continue
                if board[i][j] in seen :
                    print("failed at row check")
                    return False
                else :
                    seen.add(board[i][j])
        
        for i in range(0, 9, 3) :
            for j in range(0, 9, 3) :
                if not check_box(i, j) :
                    print(f"failed at {i} {j}")
                    return False

        return True