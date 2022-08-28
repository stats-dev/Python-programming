
# n = 2
# dp = [0] * n

# dp[1] = [1]

# for i in range(n):
#     if "()" in dp[i]:
#         dp[i] += 1
#     else:
#         pass

# print(dp[n])

from itertools import permutations # https://docs.python.org/3/library/itertools.html


test = set(permutations('()' * 3,  2 * 3)) 

result = []
result2 = []
for i in test:
    result.append(''.join(i)) # https://stackoverflow.com/questions/19641579/python-convert-tuple-to-string



for i in result: 
    i2 = i
    while '()' in i:
        i = i.replace('()', '')

        if i is '':
            result2.append(i2)
    #print(i2, '\t' + '--->', i, '\t', ':',i.count('()'))
#print(result)
print(result2)
## 시간초과 고려하라! DP 생각!