# def solution(phone_book):
#     answer = True
    
#     phone_book.sort(key=lambda x : len(x))
#     # print(phone_book)
#     for i in range(len(phone_book)):
#         chk = True
#         j = len(phone_book)-1
#         while True:
#             if len(phone_book[j]) == len(phone_book[i]):
#                 break
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 answer = False
#                 chk = False
#                 break
#             j-=1
#         if chk == False:
#             break

#     # print(answer)
#     return answer

# def solution(phone_book):
#     answer = True
#     phone_book.sort()   # 문자열 정렬 -> Ex) ["1292","25","132"] -> ["1292","132","25"] 
    
#     for i in range(len(phone_book)-1):      # i번째 문자열과 i+1번째 문자열을 비교(i번째 문자열 길이만큼)하여 같으면 answer = False
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
#             answer = False
#             break
#     return answer

def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            answer = False
        print(p1,p2)
    print(answer)
    return answer
# solution(["13", "126","137"])

# solution(["97674223", "1195524421","119"])
# solution(["119", "97674223", "1195524421"])
# solution(["123","456","789"])
solution(["12","123","1235","567","88"])
