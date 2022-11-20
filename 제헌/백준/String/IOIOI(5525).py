# n = int(input())
# m = int(input())
# s = input()
# cnt = 0

# data = 'IOI'
# data += 'OI' * (n - 1)

# for i in range(len(s) - len(data)):
#     if s[i : i + len(data)] == data:
#         cnt += 1

# print(cnt)

n = int(input())
m = int(input())
s = input()

cnt = 0
left = 0
flag = 0

while left < m - 1:
    if s[left - 1 : left + 2] == 'IOI':
        flag += 1

        if flag == n:
            flag -= 1
            cnt += 1
        
        left += 2

    else:
        left += 1
        flag = 0

print(cnt)