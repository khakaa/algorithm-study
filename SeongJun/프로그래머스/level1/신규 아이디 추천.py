import re
def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_id = re.sub('[^a-z0-9\-_.]','',new_id)
    #3단계
    new_id = re.sub('\.+','.',new_id)
    #4단계
    new_id = re.sub('^[.]|[.]$','',new_id)
    #5단계, 6단계
    new_id = 'a' if len(new_id) == 0 else new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)
    #7단계
    new_id = new_id if len(new_id) > 2 else new_id + "".join([new_id[-1] for i in range(3-len(new_id))])
    return new_id