from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n=len(online)

        graph=[[] for _ in range(n)]
        indegree=[0]*n
        mx=0

        for u,v,w in edges:
            graph[u].append((v,w))
            indegree[v]+=1
            mx=max(mx,w)

        q=deque()
        topo=[]

        for i in range(n):
            if indegree[i]==0:
                q.append(i)

        while q:
            u=q.popleft()
            topo.append(u)
            for v,w in graph[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)

        def check(limit):
            INF=10**30
            dist=[INF]*n
            dist[0]=0

            for u in topo:
                if dist[u]==INF:
                    continue

                if u!=0 and u!=n-1 and not online[u]:
                    continue

                for v,w in graph[u]:
                    if w<limit:
                        continue
                    if v!=n-1 and not online[v]:
                        continue
                    if dist[v]>dist[u]+w:
                        dist[v]=dist[u]+w

            return dist[n-1]<=k

        l,r=0,mx
        ans=-1

        while l<=r:
            mid=(l+r)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1

        return ans