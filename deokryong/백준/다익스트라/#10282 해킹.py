import sys
import heapq
input = sys.stdin.readline

T = int(input())

def dijkstra(start,end):
    distance = [INF] * (end+1)
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0
    while q:
        time, now = heapq.heappop(q)
        if distance[now] < time:
            continue
        for i in graph[now]:
            total_time = time + i[1]
            if total_time < distance[i[0]]:
                distance[i[0]] = total_time
                heapq.heappush(q,[total_time,i[0]])
    count = 0
    max = -1
    for i in range(len(distance)):
        if distance[i] != INF:
            count += 1
            if distance[i] > max:
                max = distance[i]

    return count,max

for i in range(T):
    n,d,c = map(int,input().split())
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]

    for j in range(d):
        a,b,s = map(int,input().split())
        graph[b].append([a,s])
    answer1, answer2 = dijkstra(c,n)
    print(f'{answer1} {answer2}')

