import sys
input = sys.stdin.readline

n = int(input())
words = []
dict = {}

for _ in range(n):
    words.append(input().rstrip())

for word in words: # 입력값 갯수만큼
    n_index = len(word) - 1 # 1의 자리의 경우 지수 = 0 이여야 하기 때문에 단어 길이의 -1 해준다.
    for w in word:
        if w in dict: # 딕셔너리에 문자가 있으면
            dict[w] += 10 ** n_index # 자릿수에 해당하는 만큼을 더해준다.
        else: # 딕셔너리에 아직 문자가 없으면
            dict[w] = 10 ** n_index # 자릿수를 그대로 넣어준다.
        n_index -= 1 # 문자 하나를 살펴봤으면 자릿수 -1

dict = sorted(dict.values(), reverse=True) # 딕셔너리 value 기준으로 정렬

res,m = 0,9 # 결과값, 더해줄 숫자 (9부터)

for d in dict: # 정렬한 딕셔너리 value를 큰 값부터 *9 해서 더해준다.
    res += d * m
    m -= 1

print(res)