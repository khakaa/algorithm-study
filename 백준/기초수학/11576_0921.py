# 백준 11576번 - 기초수학 - Base Conversion
## 미해결
from re import S


a, b = map(int, input().split())
m = int(input())
num = list(input().split())
result = []
s = ''
for i in num:
  n = int(i,a)
  print(n)
  while n:
    n,mod = divmod(n,b)
    s += str(mod)
  result.append(s[::-1])

print(' '.join(result))
