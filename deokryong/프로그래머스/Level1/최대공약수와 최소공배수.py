# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    def gcd(n,m):
        if n%m == 0: 
            return m
        else: 
            return gcd(m, n % m)

    answer.append(gcd(n,m))
    answer.append(n*m//gcd(n,m))
    return answer
