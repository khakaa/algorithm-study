import math
def solution(n, k):
    def find_prime(num):    # 소수 판별 함수(에라토스테네스의 체)
        chk = True
        if num == 1:        # 1은 소수가 아니므로 False 반환
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                chk = False
                break
        return chk
    answer = 0
    temp1 = ''

    div = n                      
    while True:
        if div == 0:
            break
        div,mod = divmod(div,k) # n을 k로 나눈 몫을 n, 나머지를 n1에 저장
        temp1 += str(mod)

    temp1 = temp1[::-1]     # 역순으로 바꾸어줌
    temp2 = ''
    for i in range(len(temp1)):
        if int(temp1[i]) == 0:  # temp[i]가 0이면 0이 나오기 전까지 이어붙인 값을 소수판별 
            if temp2 != '':
                if find_prime(int(temp2)):  # 소수일 경우 answer + 1
                    answer+=1   
            temp2 = ''
        else:                   # temp1[i]가 0이 아니면 temp2에 temp1[i] 이어 붙이기
            temp2 += temp1[i]
            if i == len(temp1)-1:  # 
                if find_prime(int(temp2)):  # 소수일 경우 answer + 1
                    answer+=1
    return answer

solution(939319,2)
# solution(437674,3)
# solution(110011,10)
