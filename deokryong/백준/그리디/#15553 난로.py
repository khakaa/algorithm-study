N, K = map(int,input().split())

friends = []
for i in range(N):
    friends.append(int(input()))

diff = []
for i in range(1,N):
    diff.append(friends[i] - friends[i-1])

diff.sort(reverse=True)

if N == K:
    print(N)
elif K == 1:
    print(friends[-1]+1 - friends[0])
else:
    for i in range(K-1):
        diff.pop(0)
        print(diff)
    print(N - len(diff) + sum(diff))