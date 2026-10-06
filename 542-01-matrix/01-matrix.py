# for copy import deepcopy
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows=len(mat)
        cols=len(mat[0])
        vis=[[0 for z in range(cols)] for y in range(rows)]
        dis=[[0 for z in range(cols)] for y in range(rows)]
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append([r,c,0])
                    vis[r][c]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            dis[i][j]=d
            for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_i,new_j=i+x,j+y
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if vis[new_i][new_j]==1:
                    continue
                queue.append([new_i,new_j,d+1])
                vis[new_i][new_j]=1
        return dis



        
        
        
         
        