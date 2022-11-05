n = int(input())

pos_data = []
neg_data = []
res = 0

for _ in range(n):
    num = int(input())

    if num > 0:
        pos_data.append(num)
    elif num <= 0:
        neg_data.append(num)

pos_data.sort(reverse=True)
neg_data.sort()

while pos_data:
    if len(pos_data) == 1:
        res += pos_data[0]
        pos_data.pop()
    elif (pos_data[0] * pos_data[1]) > (pos_data[0] + pos_data[1]):
        res += (pos_data[0] * pos_data[1])
        pos_data.pop(0)
        pos_data.pop(0)

    else:
        res += (pos_data[0] + pos_data[1])
        pos_data.pop(0)
        pos_data.pop(0)

while neg_data:
    if len(neg_data) == 1:
        res += neg_data[0]
        neg_data.pop()
    elif (neg_data[0] * neg_data[1]) > (neg_data[0] + neg_data[1]):
        res += (neg_data[0] * neg_data[1])
        neg_data.pop(0)
        neg_data.pop(0)

    else:
        res += (neg_data[0] + neg_data[1])
        neg_data.pop(0)
        neg_data.pop(0)

print(res)