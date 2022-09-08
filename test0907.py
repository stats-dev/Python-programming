## 직사각형에서 탈출 성공 

x,y,w,h = map(int, input().split())

print(min(x,y,w-x,h-y))