k,p,n = map(int, input().split(' '))
for _ in range(n):
    k = (k * p) % 1000000007 # 숫자가 커지면 연산시간이 오래걸리기 때문에 미리 나눠줘야함.
print(k)