# n=int(input())
# li=(list(map(int, input().split()))) # 4 1 5 2 3
# m=int(input())
# li2=(list(map(int, input().split()))) # 1 3 7 9 5

# for i in li2:
#     if i in li:
#         print(1)
#     else:
#         print(0)

""" ...시간초과... """
N=int(input())
A=list(map(int,input().split()))
M=int(input())
li=list(map(int,input().split()))
A.sort()

for num in li:
    first,last = 0, N-1
    isExist = False

    # 이분탐색 시작
    while last <= first:
        mid = (first+last)//2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > a[mid]:
            last = mid+1
        else:
            first = mid-1
    if not isExist:
        print(0)