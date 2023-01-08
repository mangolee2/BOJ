from collections import deque
import sys
input=sys.stdin.readline

def bfs(a,b):
    cnt=1
    q=deque()
    q.append((a,b))
    graph[a][b] = 0

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=0
                cnt+=1
    return cnt

N=int(input())
cnt=[]
graph=[]
for i in range(N):
    graph.append(list(map(int, input().rstrip()))) # 단지 설정
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            cnt.append(bfs(i,j)) # 모든 그래프를 모두 방문해주되, 1이 있으면 bfs실행
print(len(cnt))
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])
