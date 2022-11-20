def solution(cacheSize, cities):
    answer = 0
    q = []
    
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            
            if len(q) < cacheSize:
                q.append(city)
                
            else:
                if cacheSize != 0:
                    q.pop(q.index(city))
                    q.append(city)
                
        else:
            answer += 5
        
            if len(q) < cacheSize:
                q.append(city)
                
            else:
                if cacheSize != 0:
                    q.pop(0)
                    q.append(city)

    return answer