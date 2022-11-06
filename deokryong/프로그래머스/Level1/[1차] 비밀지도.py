def solution(n, arr1, arr2):
    answer = [''] * n
    #1단계 - 지도 1 해독
    temp_arr1 = [(['']*n) for i in range(n)]
   
    for i in range(n):
        temp = arr1[i]
        st = ''
        while temp != 0:
            div, mod = divmod(temp,2)
            temp = div
            st += str(mod)
        while len(st) != n:
            st+='0'
        for j in range(n):
            if st[n-j-1] == '0':
                temp_arr1[i][j] = ''
            else:
                temp_arr1[i][j] = '#'
                
    #2단계 - 지도 2 해독
    temp_arr2 = [(['']*n) for i in range(n)]
   
    for i in range(n):
        temp = arr2[i]
        st = ''
        while temp != 0:
            div, mod = divmod(temp,2)
            temp = div
            st += str(mod)
        while len(st) != n:
            st+='0'
        for j in range(n):
            if st[n-j-1] == '0':
                temp_arr2[i][j] = ''
            else:
                temp_arr2[i][j] = '#'
                
    #3단계 - 해독한 지도 겹치기
    for i in range(n):
        for j in range(n):
            if temp_arr1[i][j] == '#' or temp_arr2[i][j] == '#':
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer