class Solution:
    def dfs(self,r,c,vis,rows,cols,board):
        if r<0 or r>=rows or c<0 or c>=cols:
            return 
        if board[r][c]=="X":
            return
        if vis[r][c]==1:
            return 
        vis[r][c]=1
        self.dfs(r-1,c,vis,rows,cols,board)        
        self.dfs(r,c-1,vis,rows,cols,board)        
        self.dfs(r,c+1,vis,rows,cols,board)        
        self.dfs(r+1,c,vis,rows,cols,board)        


    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        vis=[[0 for z in range(cols)] for y in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if board[r][c]=="O":
                        if vis[r][c]==0:
                            self.dfs(r,c,vis,rows,cols,board)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and vis[r][c]==0:
                    board[r][c]="X"
        
    

