n,m=map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input()))) # 맵 정보 입력

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False # 주어진 범위 벗어나는 경우 즉시 종료시키기
    if graph[x][y]==0:
        graph[x][y]=1 # 해당 노드 방문 처리해주고 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y) # 재귀로 네방향 모두 0인지 탐색, 묶어줌
        return True
    return False
# bfs def 함수로 정의해주고 나서

result = 0
for i in range(n):
    for j in range(m): # 맵돌기
        if dfs(i,j) == True:
            result += 1
print(result)
