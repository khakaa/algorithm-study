T = int(input())
for i in range(1,T+1):
    N = input()
    result = []
    k = 0
    while [0,1,2,3,4,5,6,7,8,9] != result:
        k+=1
        answer = int(N) * k
        for j in range(len(str(answer))):
            if int(str(answer)[j]) not in result:
                result.append(int(str(answer)[j]))
                result = sorted(result)
    print(f'#{i} {answer}')
    