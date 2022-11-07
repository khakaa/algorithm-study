N, K = map(int, input().split(' '))
stuff = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split(' '))))

# O(N) * O(K)
for i in range(1, N+1): # 물품의 수만큼
    weight = stuff[i][0] # 현재 돌고 있는 물품 무게
    value = stuff[i][1] # 현재 돌고 있는 물품 가치

    for j in range(1, K+1): # 1부터 들 수 있는 최대 가치까지         
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            # 현재 물건을 넣은 뒤 남은 무게를 채울 수 있는 최댓값, 현재 물건을 넣어주는 것보다 다른 물건들로 채우는 값 중 최댓값            
            # max(현재물건가치 + knapsack[이전물건][현재가방무게 - 현재물건무게], knapsack[이전물건][현재가방무게])
            knapsack[i][j] = max(value + knapsack[i-1][j - weight], knapsack[i-1][j])

print(knapsack[N][K])