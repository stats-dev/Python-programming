N = int(input())
first = 666 # 초기값
while N != 0: # N 이 0이 아니면 계속 반복
    try:
        if '666' in str(first): # 만약 666이란 문자열이 문자열(first)안에 있으면
            N -= 1    # N을 1 감소시키고
    except N == 0:
        break
    first += 1 #first의 값을 1 증가시킨다.
print(first)