N, M = map(int, input().split())
chess = []
cnt = []

[chess.append(input()) for _ in range(N)]

for a in range(N-7):
    for b in range(M-7):
        ind1 = 0
        ind2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        ind1 += 1
                    if chess[i][j] != 'B':
                        ind2 += 1
                else:
                    if chess[i][j] != 'B':
                        ind1 += 1
                    if chess[i][j] != 'W':
                        ind2 += 1
        cnt.append(min(ind1, ind2))

print(min(cnt))