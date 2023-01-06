from collections import deque
import sys

N,M=map(int, input().split())
graph=[]

for _ in range(N):
    graph.append(list(map(int, input()))) # for문 2개 노, n=4만 돌아 그래프 생성

def bfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    q=deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >=N or ny <0 or ny >=M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0,0))