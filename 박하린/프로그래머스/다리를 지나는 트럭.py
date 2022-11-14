from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0 for _ in range(bridge_length)])
    ans = 0
    t_sum = 0
    flag = True

    while flag:
        pop_value = queue.popleft()
        t_sum -= pop_value

        # 트럭 다리 건너기 가능
        if t_sum + truck_weights[0] <= weight:
            t_sum += truck_weights[0]
            queue.append(truck_weights.pop(0))
        # 트럭 다리 건너기 불가능
        else:
            queue.append(0)

        # 시간 계산
        ans += 1

        if len(truck_weights) == 0:
            ans += bridge_length
            flag = False
    return ans

print(solution(2,10,[7,4,5,6]))
print(solution(100,	100,	[10]))