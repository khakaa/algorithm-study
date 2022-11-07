n = int(input())
ti = [0,1,2]+([0]*998)
for i in range(3,n+1):
    ti[i]=ti[i-1]+ti[i-2]
    ti[i]=ti[i]%10007
print(ti[n])