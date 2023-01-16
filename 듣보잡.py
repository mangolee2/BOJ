import sys
input=sys.stdin.readline

a,b=map(int,input().split()) # 3 4 : 듣지도, 보지도 못한 사람 수

hear=[]
see=[]
for i in range(a):
    hear.append((input()))
for i in range(b):
    see.append((input()))

ans=list(set(hear) & set(see)) # set으로 풀어준다음, & 교집합으로 묶어줌

ans.sort()
print(len(ans))
print(''.join(ans), end='')