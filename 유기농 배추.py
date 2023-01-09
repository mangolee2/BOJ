from collections import deque
import sys
input=sys.stdin.readline

def bfs(a,b):
    q=deque()
    q.append((a,b))
    graph[a][b]=0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx <0 or nx >= n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0
    return

dx=[-1,1,0,0]
dy=[0,0,-1,1]

t=int(input()) # 2

for i in range(t):
    n,m,k=map(int, input().split()) # 10 8 7
    graph=[[0]*(m) for _ in range(n)]
    cnt=0

    for j in range(k): # 엣지 관계성
        x,y=(map(int, input().split()))
        graph[x][y]=1
    
    for a in range(n):
        for b in range(m):
            if graph[a][b]==1:
                bfs(a,b)
                cnt += 1

print(cnt)
