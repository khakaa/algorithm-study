n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0]

def rec(x, y, n):
    base_color = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if base_color != graph[i][j]:
                rec(x, y, n // 2)
                rec(x, y + n // 2, n // 2)
                rec(x + n // 2, y, n // 2)
                rec(x + n // 2, y + n // 2, n // 2)
                return
    if base_color == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1

rec(0, 0, n)

for i in cnt:
    print(i)