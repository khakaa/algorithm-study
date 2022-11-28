N = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

min_cost = price[0]

result = min_cost * dist[0]

for i in range(1,N-1):
    if price[i] <= min_cost:
        min_cost = price[i]
        result += min_cost * dist[i]
    else:
        result += min_cost * dist[i]
print(result)