## 백준: 전깃줄
N = int(input())


test = []
dp = [1] * N

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
        
print(N-max(dp))


# ### https://seohyun0120.tistory.com/entry/가장-긴-증가하는-부분-수열LIS-완전-정복-백준-파이썬
# # 11053번
# x = int(input())

# arr = list(map(int, input().split()))

# dp = [1 for i in range(x)]

# for i in range(x):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))
# ###
# test = [(1, 8), (3, 9), (2, 2), (4, 1), (6, 4), (10, 10), (9, 7), (7, 6)]

# #print(sorted(test, key=lambda tup: tup[0])) ## 튜플 안에서 순서를 처음 요소를 기준으로 다시 잡고 정렬한다.

# test1 = sorted(test, key=lambda tup: tup[0])
# #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index

# ## 여기서부터, 이전 전못대 기준으로 다음 전못대가 더 큰 수에 해당하는 전못대에 연결된 경우를 찾는다.
# ## 그냥, B에 해당하는 모든 전깃줄의 순서를 살펴보는 게 필요하다.
# result = 0

# for i in range(8):
#     result += (test1[i][1] < test1[i-1][1])

# print(result)