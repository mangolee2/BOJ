""" bfs문제이므로 deque 를 사용합니다 """
from collections import deque 
# 괴물 맵 형성 
n,m=map(int, input().split())
graph=[]
for i in range(n): # 행수만큼 입력
    graph.append(list(map(int, input()))) # 맵 만들기
      
# 네 방향 탐색 
dx=[-1,1,0,0]
dy=[0,0,1,-1]

# bfs def 함수를 정의해준다
def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    # 큐가 빌 때까지 반복
    while queue: # 큐가 0이 될때까지
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0: # 괴물이 있다
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append( (nx,ny) )
    return graph[n-1][m-1] # 가장 오른쪽 아래까지의 최단 거리를 반환해준다

print(bfs(0,0))


