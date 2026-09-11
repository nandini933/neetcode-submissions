class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # we need uniqueness per row -> {}
        # we need uniqueness per coloumn -> {}
        # we need uniquness per box -> {r//3,c//3}
        # valid inputs are already mentioned -> 1-9 or also contains "."

        # also for nested lists, it is key to understand the order in which we intend on doing the parsing through or looking into really... essentially row based is one row at a time...
        r = defaultdict(set)
        c = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    continue
                if (board[row][col] in r[row] or 
                    board[row][col] in c[col] or 
                    board[row][col] in boxes[(row//3,col//3)]):
                    return False
                r[row].add(board[row][col])
                c[col].add(board[row][col])
                boxes[(row//3,col//3)].add(board[row][col])
        return True