# 증가하는 수열이면서 & 배열의 합이 최대치일 경우.
size = int(input())
array = list(map(int,input().split(' ')))
total = [1]*size
total[0] = array[0]
for i in range(1,size):
    for j in range(i):
        if array[j]<array[i]:
            total[i] = max(total[i],total[j]+array[i])
        else:
            total[i]=max(total[i],array[i])
print(max(total))