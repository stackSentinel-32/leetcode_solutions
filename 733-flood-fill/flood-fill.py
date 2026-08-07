class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        vis=deepcopy(image)
        r=len(vis)
        c=len(vis[0])
        initial_color=vis[sr][sc]
        self.dfs(sr,sc,color,initial_color,vis,r,c)
        return vis

    def dfs(self,i,j,new_color,initial_color,vis,r,c):
        if i<0 or i>=r or j<0 or j>=c:
            return 
        if vis[i][j]!=initial_color:
            return 
        if vis[i][j]==new_color:
            return 
        vis[i][j]=new_color

        self.dfs(i+1,j,new_color,initial_color,vis,r,c)
        self.dfs(i,j-1,new_color,initial_color,vis,r,c)
        self.dfs(i-1,j,new_color,initial_color,vis,r,c)
        self.dfs(i,j+1,new_color,initial_color,vis,r,c)
