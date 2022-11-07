import collections

N,M = map(int,input().split())

arr = [''] * N
for i in range(N):
    arr[i] = input()

arr.sort()

result = []
count = 0
for i in range(M):
    temp = [''] * N
    for j in range(N):
        temp[j] = arr[j][i]
    count += (N-sorted(collections.Counter(temp).most_common(),key=lambda x:(-x[1],x[0]))[0][1])
    result.append(sorted(collections.Counter(temp).most_common(),key=lambda x:(-x[1],x[0]))[0][0])

print("".join(result))
print(count)



