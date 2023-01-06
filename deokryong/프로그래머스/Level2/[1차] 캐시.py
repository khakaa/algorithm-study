from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_arr = deque()

    if cacheSize == 0:                  # cacheSize가 0일 경우에는 항상 cache miss이므로
        answer = len(cities) * 5
    else:                               # cacheSize가 0이 아닐 경우
        for i in range(len(cities)):        
            if len(cache_arr) < cacheSize: # cache_arr의 크기가 cacheSize보다 작을경우
                if len(cache_arr) != 0 and cities[i].lower() in cache_arr:      # 예를들어 cacheSize가 2이고 현재 cach_arr에 Jeju밖에 안들어가 있을 경우 -> 다음 citie가 Jeju이면 answer += 1을 해줘야하므로
                    answer += 1
                    del cache_arr[cache_arr.index(cities[i].lower())]
                else:
                    answer += 5
                cache_arr.append(cities[i].lower())
            else:                          # cahce_arr의 크기가 cacheSize일 경우(이미 캐시가 다 찬 상황)
                if cities[i].lower() in cache_arr:
                    answer += 1
                    del cache_arr[cache_arr.index(cities[i].lower())]
                else:
                    answer += 5
                    cache_arr.popleft()
                cache_arr.append(cities[i].lower())
                
    print(answer)
    return answer

solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2,["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(1,["Jeju", "Pangyo", "Seoul", "NewYork", "newyork"])


