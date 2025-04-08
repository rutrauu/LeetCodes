from collections import defaultdict
from typing import List

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    col = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            current = board[r][c]
            if current == ".":
                continue

            if (current in rows[r] or 
                current in col[c] or 
                current in boxes[(r // 3, c // 3)]):
                return False

            rows[r].add(current)
            col[c].add(current)
            boxes[(r // 3, c // 3)].add(current)

    return True

print(isValidSudoku(board))

