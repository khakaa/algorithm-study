import sys
input = sys.stdin.readline

lights = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}

t = int(input())
for _ in range(t):
    total_cnt = 0
    a,b = input().rstrip().split(' ')
    a = (5 - len(a))*" " + a
    b = (5 - len(b))*" " + b
    
    for i in range(5):
        for j in range(7):
            total_cnt += (lights[a[i]][j] != lights[b[i]][j])
    print(total_cnt)