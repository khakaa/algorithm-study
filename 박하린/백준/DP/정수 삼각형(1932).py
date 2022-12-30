n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split(' '))))

for i in range(1, n):
    for j in range(len(tri[i])):
        if i == 1:
            tri[i][j] += tri[0][0]
        else:
            if j == 0:
                tri[i][j] += tri[i-1][0]
            elif j == len(tri[i])-1:
                tri[i][j] += tri[i-1][len(tri[i-1])-1]
            else:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))