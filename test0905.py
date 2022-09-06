"""
## 구구단
 N = int(input())

for i in range(1, 9+1):
    print(N, "*", i, "=", N * i)
 """

""" ## 주석 alt + shift + a
### N 찍기
N = int(input())

for i in range(1,N+1):
    print(i) """


""" ## 윤년
N = int(input())

if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
    print(1)
else:
    print(0) """


""" 
## 알람 시계
H, M = map(int, input().split())
if M >= 45:
    print(H, M - 45)
elif H >= 1 and M < 45:
    print(H-1, M - 45 + 60)
elif H < 1 and M < 45:
    print(H -1 + 24, M - 45 + 60)
else:
    print("error")
 """

""" 
## 기찍
N = int(input())

for i in range(N):
    print(N-i) """


""" ## 상수

A, B = map(str, input().split())
if int(A[::-1]) > int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1]) """
""" 

## 음계
ascend =['1', '2', '3', '4', '5', '6', '7', '8']
t = input().split()
#print(t, ascend)
if t == ascend:
    print("ascending")
elif t == ascend[::-1]:
    print("descending")
else:
    print("mixed")
 """
""" 
### 나머지
result = []
test = []
for i in range(10):
    result.append(int(input()))

for num in result:
    test.append(num % 42)
    
t1 = set(test)
print(len(t1))
 """


""" ## OX 퀴즈

N = int(input())
test = []

for i in range(N):
    test.append(input())

for num in test:
    sum = 0
    score = 1
    for j in num:
        if j == 'O':
            sum += score
            score += 1
        else:
            score = 1
    print(sum)

 """


""" ## 시험성적
N = int(input())

if N >= 90:
    print("A")
elif N >= 80:
    print("B")
elif N >= 70:
    print("C")
elif N >= 60:
    print("D")
else:
    print("F") """

""" 
### 고양이
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
 """


 
## 개 : "" 큰따옴표가 에러가 많아서, '' 작은따옴표 쓴다.
# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\__|')

""" 
## 알파벳 찾기
S = input()

## find 함수로 한방에 해결 가능하다.
alphabet = list(range(97,123)) ### 아스키코드 대응 알파벳 확인

for i in alphabet:
    print(S.find(chr(i)))
 """

""" ## 최소, 최대
N = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums)) """

""" 
### 사칙연산
A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

 """


""" 
## X보다 작은 수
N, X = map(int, input().split())
A = input().split()

#print(A)
result = [c for c in A if int(c) < X]
print(' '.join(result))
 """


""" ## A+B-3
T = int(input())
result = []
for i in range(T):
    A, B = map(int, input().split())
    result.append(A + B)

for num in result:
    print(num)

 """

""" 

## A+B -4

while 1:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

 """

""" 
## A+B -5

while 1:
    try:
        A, B = map(int, input().split())
        if A and B != 0:
            print(A+B)
        else:
            break
    except:
        break
 """
""" 
## A X B
A, B = map(int, input().split())
print(A*B)
 """
""" 
## 아스키코드 출력
test = input()

print(ord(test))
 """


## 숫자의 합
N = int(input())
S = input()
result = []
D = 0

for i in range(N):
    result.append(S[i])

for j in range(N):
    D += int(result[j])

print(D)


