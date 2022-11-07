k = int(input())
data = list(map(int, input().split()))
graph = [[] for _ in range(k + 1)]

def binary_tree(arr, x):
    mid = len(arr) // 2
    graph[x].append(arr[mid])

    if len(arr) == 1:
        return

    binary_tree(arr[:mid], x + 1)
    binary_tree(arr[mid + 1:], x + 1)

binary_tree(data, 1)

for i in range(1, k + 1):
    print(*graph[i])