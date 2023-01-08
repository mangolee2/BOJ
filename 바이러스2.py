from collections import deque

n=int(input())
e=int(input())
graph=[[0]*(n+1) for _ in range(n+1)] # 그래프 초기화는 왜??
visited=[0]*(n+1) # 방문 초기화 0 -> 방문했으면 1

for _ in range(e): # 관계성 설정
    a,b=map(int, input().split())
    graph[a][b]=graph[b][a]=1

q=deque()
q.append(1)
visited[1]=1
cnt=0
while q:
    v=q.popleft()

    for i in range(1, n+1):
        if graph[v][i]==1 and visited[i]==0:
            q.append(i)
            visited[i]=1
            cnt += 1
print(cnt)