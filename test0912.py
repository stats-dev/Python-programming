
while 1:
    try:
        N = input()
        if N == '0':
            break
        elif N == N[::-1]:
            print("yes")
        else:
            print("no")
    except:
        break
