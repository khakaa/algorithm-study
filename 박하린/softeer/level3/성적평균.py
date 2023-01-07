import sys

input = sys.stdin.readline
n,k = map(int, input().rstrip().split())
student = list(map(int, input().rstrip().split()))
for _ in range(k):
    a,b = map(int, input().rstrip().split())
    sec = student[a-1:b]
    print(format(round(sum(sec)/len(sec),2), '.2f'))

