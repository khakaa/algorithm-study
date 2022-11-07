import heapq

n, e = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

orig_dist = dijkstra(1)
first_dist = dijkstra(u)
second_dist = dijkstra(v)

u_cost = orig_dist[u] + first_dist[v] + second_dist[n]
v_cost = orig_dist[v] + second_dist[u] + first_dist[n]

res = min(u_cost, v_cost)

if res < INF:
    print(res)
else:
    print(-1)