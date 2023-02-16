import sys
input = sys.stdin.readline

k,p,n = map(int, input().rstrip().split())

# 재귀함수 구현 
# 시간복잡도 O(logN)
# recursive(2, 10)            ->  2**10
# -> recursive(2, 5) * recursive(2, 5)              -> 2**5
# -> recursive(2, 2) * recursive(2, 2) * 2                 -> 2**2 * 2
#    * recursive(2, 2) * recursive(2, 2) * 2               -> 2**2 * 2

def recursive(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        f = recursive(x, y / 2)
        return f * f % 1000000007
    else:
        f = recursive(x, y // 2)
        return f * f * x % 1000000007

print(k * recursive(p, n*10) % 1000000007)