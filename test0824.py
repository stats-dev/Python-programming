
## 2577 
## 3개 자연수에서 그 곱의 결과에서 0부터 9까지 각각 숫자 몇번 쓰였는지 차례로 한 줄에 하나씩 출력한다.


nums = []
results = 1
for i in range(3):
    nums.append(int(input()))


for num in nums:
    results *= num

#print(results)

from collections import Counter

test = {}

test1 = Counter(str(results))

for i in range(10):
    test[str(i)] = 0

for j,v in test1.items():
    if j in test:
        test[j] = v
    else:
        pass

for i,v in test.items():
    print(v)