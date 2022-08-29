

# def recursive(result, s, open, close):
#     if (open == 0 and close == 0):
#         result.append(s)
#         return result

#     if (open > 0):
#         recursive(result, s + "(", open - 1, close)

#     if (close > open):
#         recursive(result, s + ")", open, close - 1)



# result = []
# recursive(result, "(", 3 - 1, 3)
# print(result)


result = []

def recursive(result, s, open, close):
    if (open == 0 and close == 0):
        result.append(s)
        return result

    if (open > 0):
        recursive(result, s + "(", open - 1, close)

    if (close > open):
        recursive(result, s + ")", open, close - 1)

recursive(result, "", 3, 3)
print(result)
