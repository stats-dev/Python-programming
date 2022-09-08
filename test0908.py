""" 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로 """

N = int(input())
words = set()
for i in range(N):
    word = input()
    words.add(word)


test = list(words)

test.sort() ## 알파벳 순서 출력1
test.sort(key=len) ## 요소 길이에 따라 출력2


for element in test:
    print(element)