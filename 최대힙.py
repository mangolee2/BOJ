import heapq
import sys

n=int(input())
heap=[]

#max heap 
for _ in range(n):
    i=int(input())
    if i != 0:
        heapq.heappush(heap, (-i))
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)