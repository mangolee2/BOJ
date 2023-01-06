from collections import deque
import sys

input=sys.stdin.readline

def bfs(v): # 정점 v
    q = deque()
    q.append(v)
    visited[v]=1 # 정점 v를 방문했다면, 1
    while q:
        v = q.popleft()
        print(v, end=' ') # 방문한 v 출력
        
        for i in range(1, n+1):
            if visited[i]==0 and graph[v][i]==1:
                q.append(i)
                visited[i] = 1

n,m,v = map(int, input().split()) # 4 5 1: 정점 엣지 시작 
graph=[[0]*(n+1) for _ in range(n+1)] # 0으로 채워진 graph 생성
visited = [0]*(n+1)

for _ in range(m): # 엣지 돌면서
    a,b = map(int, input().split()) # 엣지 관계들 입력
    graph[a][b] = graph[b][a] = 1

bfs(v) # bfs 실행 
