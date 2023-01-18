n,k=map(int,input().split())
result = 0

while True:
    target = (n//k)*k  # (n==k 로 나누어 떨어지는 수)가 될 때까지 1씩 빼기 
    result += (n-target)
    n = target
    print(target, result, n)


    if n < k:  # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        break

    result += 1
    n//=k

result += (n-1)  # 마지막으로 남은 수에 대하여 1씩 빼기 
print(result)