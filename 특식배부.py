n=int(input())
li=list(map(int, input().split())) # a,b,c

total=0
for i in li:
    if i <= n:
        total += int(i)
    else:
        i = n
        total += int(i)
print(total)