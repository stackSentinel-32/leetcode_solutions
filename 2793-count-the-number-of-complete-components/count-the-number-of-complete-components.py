class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        vis=[False]*n
        ans=0
        for i in range(n):
            if vis[i]:
                continue
            st=[i]
            vis[i]=True
            c=0
            e=0
            while st:
                u=st.pop()
                c+=1
                e+=len(g[u])
                for v in g[u]:
                    if not vis[v]:
                        vis[v]=True
                        st.append(v)
            if e==c*(c-1):
                ans+=1
        return ans