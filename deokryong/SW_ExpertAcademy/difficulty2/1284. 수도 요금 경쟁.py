T = int(input())
for i in range(1,T+1):
    P,Q,R,S,W = map(int,input().split())
    A = W * P
    B = 0
    if W <= R:
        B = Q
    else:
        B = Q + (W-R)*S
   
    result = A if A<B else B
    print(f'#{i} {result}')