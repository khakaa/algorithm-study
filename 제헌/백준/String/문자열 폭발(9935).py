# 시간 : 548ms
# s = input()
# data = input()
# res = []

# for i in range(len(s)):
#     res.append(s[i])

#     if ''.join(res[-len(data) : ]) == data:
#         for _ in range(len(data)):
#             res.pop()

# print('FRULA' if len(res) == 0 else ''.join(res))

# 시간 : 240ms
# if문 안에서 res 스택과 폭발 문자열 비교의 차이?
s = input()
data = input()
res = []

for i in range(len(s)):
    res.append(s[i])

    if res[-1] == data[-1] and ''.join(res[-len(data) : ]) == data:
        for _ in range(len(data)):
            res.pop()

print('FRULA' if len(res) == 0 else ''.join(res))