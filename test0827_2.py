N = int(input())


test = []
dp = [0] * N ## 0으로 변경해보면, 아래는 값이 바껴야 한다.

for i in range(N):
    A,B = map(int, input().split())
    test.append((A,B))


arr = sorted(test, key=lambda tup: tup[0])
# print(test)
# print(arr)

for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]: ## 오른쪽 전못대를 기준으로 가져간다.
            dp[i] = max(dp[i], dp[j]+1)
        
print(N-max(dp)-1)
