T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    arr[0][0] = 1
    position = [0,0]
    value = 2
    def right():
        global value
        while True:
            if position[1]+1 == N or arr[position[0]][position[1]+1] != 0:
                
                break
            position[1] += 1
            arr[position[0]][position[1]] = value
            value += 1
            
    def left():
        global value
        while True:
            if position[1]-1 == -1 or arr[position[0]][position[1]-1] != 0:
                break
            position[1] -= 1
            arr[position[0]][position[1]] = value
            value += 1
    def up():
        global value
        while True:
            if arr[position[0]-1][position[1]] != 0:
                break
            position[0] -= 1
            arr[position[0]][position[1]] = value
            value += 1
    def down():
        global value
        while True:
            if position[0]+1 == N or arr[position[0]+1][position[1]] != 0:
                break
            position[0] += 1
            arr[position[0]][position[1]] = value
            value += 1
    chk = False
    while True:
        for k in range(N):
            if N*N in arr[k]:
                chk = True
                break
        if chk:
            break
        right()
        down()
        left()
        up()
    
    print(f'#{i}')
    for j in range(N):
        for k in range(N):
            if k==N-1:
                print(arr[j][k])
            else:
                print(arr[j][k],end=" ")
            