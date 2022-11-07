def solution(n):
    answer = 0
    cnt_1 = bin(n)[2:].count('1')
    
    while n <= 1000000:
        n += 1
        res = bin(n)[2:].count('1')
        
        
        if cnt_1 == res:
            break
            
    return n