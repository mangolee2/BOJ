from collections import deque
m,n=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))

q=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j)) # 어느 곳에 있든지 1이면 큐에 넣어놓고, 시작 

dx,dy=[-1,1,0,0],[0,0,-1,1]

while q:
    x,y = q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            q.append((nx,ny))
            graph[nx][ny]=graph[x][y] + 1

flag = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag=True
            break
if flag:
    print(-1)
else:
    print(max(map(max,graph))-1)