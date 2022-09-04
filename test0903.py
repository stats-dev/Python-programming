
## 백준
T = int(input())


for _ in range(T):
    R, S = input().split()
    for j in S:
        print(j*int(R), end='') ### end=''의 의미!!! 옆으로 붙이겠따..
    print()



#print(replist, list(seqs))



# print(S[0] * int(R[0]))
# print(S[1] * int(R[1]))
### 