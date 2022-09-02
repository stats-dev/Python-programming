
## 재귀 이해하기
def sum_num(end_num):
	sum = 0
	for i in range(1, end_num):
		sum += i
	return sum

print(sum_num(100))