import sys

K, N = map(int, input().split())
K_cm = []

# K 길이 입력
for i in range(K):
  K_cm.append(int(sys.stdin.readline()))

# 합/K == 랜선최대길이(Ans) 로 각각 길이들을 나눴을 때 N이 되는지 확인해보고
# 안되면 랜선최대길이(Ans)를 줄인다.
Ans = sum(K_cm)//K
while(1):
  x = 0
  for i in K_cm:
    x += i//Ans
  if x == N:
    print(Ans)
    break
  Ans -= 1