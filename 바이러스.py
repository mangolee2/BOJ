from collections import deque

n=int(input())
e=int(input())
graph=[[0]*(n+1) for i in range(n)]
visited = [0 for i in range(n)]

for i in range(e): # 관계성 성립
    a,b=map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = 1
def dfs(v):
    visited[v]=1
    for i in range(n): # 정점 만큼 돌면서
        if graph[v][i]==1 and visited[i]==0:
            dfs(i)
dfs(0)
cnt=0
for i in range(1,n): # 1번을 제외하고 
    if visited[i]==1:
        cnt += 1
print(cnt)