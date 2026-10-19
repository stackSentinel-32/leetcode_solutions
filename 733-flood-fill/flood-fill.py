class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row=len(image)
        col=len(image[0])
        ini_color=image[sr][sc]

        if ini_color==color:
            return image

        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col:
                return 
            if image[i][j]!=ini_color or image[i][j]==color:
                return 
                
            image[i][j]=color
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        dfs(sr,sc)
        return image

        
#         if image[sr][sc]==color:
#             return image
#         vis=deepcopy(image)
#         r=len(vis)
#         c=len(vis[0])
#         initial_color=vis[sr][sc]
#         self.dfs(sr,sc,color,initial_color,vis,r,c)
#         return vis

#     def dfs(self,i,j,new_color,initial_color,vis,r,c):
#         if i<0 or i>=r or j<0 or j>=c:
#             return 
#         if vis[i][j]!=initial_color:
#             return 
#         if vis[i][j]==new_color:
#             return 
#         vis[i][j]=new_color

#         self.dfs(i+1,j,new_color,initial_color,vis,r,c)
#         self.dfs(i,j-1,new_color,initial_color,vis,r,c)
#         self.dfs(i-1,j,new_color,initial_color,vis,r,c)
#         self.dfs(i,j+1,new_color,initial_color,vis,r,c)
