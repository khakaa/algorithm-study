from collections import deque

def return_AC(func_name, arr):
    r_cnt = 0
    for n in func_name:
        if n == 'D' and len(arr) == 0:
            return 'error'
        
        if n == 'R':
            r_cnt += 1
        
        elif n == 'D':
            if r_cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if r_cnt % 2 == 1:
        arr.reverse()
    return arr

T = int(input()) 
ans = []
for _ in range(T):
    func_name = input()
    arr_len = int(input())
    arr = input()
    if arr_len == 0:
        arr = deque()
        ans.append(return_AC(func_name, arr))
    else:
        arr = deque(arr[1:len(arr)-1].split(','))
        ans.append(return_AC(func_name, arr))

for a in ans:
    if a != 'error':
        print("["+','.join(a)+"]")
    else:
        print(a)