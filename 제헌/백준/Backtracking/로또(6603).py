def lotto(start, length):
    if length == 6:
        print(*target)
        return
    
    for i in range(start, n):
        target.append(data[i])
        lotto(i + 1, length + 1)
        target.pop()

while True:
    n, *data = map(int, input().split())
    target = []

    if n == 0:
        break

    lotto(0, 0)
    print()