import sys

input = sys.stdin.readline
n,m = map(int, input().split(' '))
name = []
meeting = {}
for _ in range(n):
    name.append(input().rstrip())
    meeting[name[-1]] = []
name.sort()
for _ in range(m):
    m_info = input().rstrip().split(' ')
    meeting[m_info[0]].append((int(m_info[1]), int(m_info[2])))

for key,value in meeting.items():
    reserved = sorted(value, key=lambda x : x[0])
    ans = []
    for i in range(len(reserved)):
        # 첫 회의가 9시인지 체크
        if i == 0:
            if reserved[i][0] > 9:
                ans.append('09-{}'.format(reserved[i][0]))
            if len(reserved) == 1:    
                if reserved[i][1] < 18:
                    ans.append('{}-18'.format(reserved[i][1]))
        # 첫 회의 아닐 경우
        else:
            if start < reserved[i][0]:
                ans.append('{}-{}'.format(start,reserved[i][0]))
            # 마지막 회의일 경우
            if i == len(reserved)-1 and reserved[i][1] < 18:
                ans.append('{}-18'.format(reserved[i][1]))
        start = reserved[i][1]
    if len(reserved) == 0:
        ans.append('09-18')
    meeting[key] = ans

for i in range(n):
    print('Room {}:'.format(name[i]))
    if len(meeting[name[i]]) > 0:
        print('{} available:'.format(len(meeting[name[i]])))
        for value in meeting[name[i]]:
            print(value)
    else:
        print('Not available')
    if i < n-1:
        print('-----')