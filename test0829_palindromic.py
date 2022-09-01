
s = "cabb"

#print(s[::-1], s)

result = []

# print(list(s), list(s[::-1]))

# for i in range(len(s)):
#     if list(s)[i] == list(s[::-1])[i]:
#         result.append(list(s)[i])

# print(''.join(result))

for i in range(len(s)):
    if list(s)[i] in list(s[::-1])[i]:
        result.append(list(s)[i])
    else:
        s = s[:len(s)-1]
        

print(''.join(result))