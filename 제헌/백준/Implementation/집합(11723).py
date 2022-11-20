import sys
input = sys.stdin.readline
m = int(input())
s = set()

for _ in range(m):
    data = input().strip().split()

    if len(data) == 1:
        first = data[0]
    else:
        first, second = data[0], data[1]
        second = int(second)

    if first == 'add':
        s.add(second)

    elif first == 'remove':
        s.discard(second)

    elif first == 'check':
        print(1 if second in s else 0)

    elif first == 'toggle':
        if second in s:
            s.discard(second)
        else:
            s.add(second)

    elif first == 'all':
        s = set([i for i in range(1, 21)])
    
    else:
        s.clear()