t = int(input())
# 우 -> 하 -> 좌 -> 상
dxy = [[0,1],[1,0],[0,-1],[-1,0]]

for t in range(t):
    n = int(input())
    snail = [[0 for _ in range(n)] for _ in range(n)]
    x,y = 0,0
    dist = 0

    for i in range(1,n*n+1):
        snail[x][y] = i
        x += dxy[dist][0]
        y += dxy[dist][1]

        if x < 0 or x >= n or y < 0 or y >= n or snail[x][y] != 0:
            x -= dxy[dist][0]
            y -= dxy[dist][1]

            dist = (dist + 1) % 4

            x += dxy[dist][0]
            y += dxy[dist][1]
    
    print("#{}".format(t+1))
    for s in snail:
        print(*s)
