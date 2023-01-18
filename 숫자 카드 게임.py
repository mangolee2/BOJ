n,m=map(int, input().split())

result = 0
for i in range(n):
    data=list(map(int, input().split())) # append 로 미리 할당안해주고 list로 저장

    min_value=min(data)
    result = max(result, min_value)

    print(result)
