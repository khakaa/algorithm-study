T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(list(map(int,input().split())))
    temp_90_row = N-1
    temp_90_col = 0
    
    temp_180_row = N-1
    temp_180_col = N-1
    
    temp_270_row = 0
    temp_270_col = N-1

    print(f'#{i}')
    st_90 = ''
    st_180 = ''
    st_270 = ''
    
    for j in range(N):   
        for k in range(N):
            st_90 += str(arr[temp_90_row][temp_90_col])
            st_180 += str(arr[temp_180_row][temp_180_col])
            st_270 += str(arr[temp_270_row][temp_270_col])
            temp_90_row-=1
            temp_180_col-=1
            temp_270_row+=1
        print(f'{st_90} {st_180} {st_270}')
        st_90 = ''
        st_180 = ''
        st_270 = ''

        temp_90_row = N-1
        temp_180_col = N-1
        temp_270_row = 0

        temp_90_col += 1
        temp_180_row -= 1
        temp_270_col -= 1
         
