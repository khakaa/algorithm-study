n = int(input())
a = [0,1,3,5]+[0]*997
for i in range(3,1001):
    a[i]=(a[i-1]+(a[i-2]*2))
print(a[n]%10007)