a, b = map(int,input().split())
for i in range(min(a,b),(a*b)+1):
    if a%i == 0 and b%i == 0:
        print(i)
        break

for i in range(max(a,b),(a*b)+1):
    if i%a==0 and b%i==0:
        print(i)
        break

# 위코드는 시간초과(효율성검사 탈락)뜸...
# 나중에 다시...