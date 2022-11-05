n = int(input())
file_dict = {}

for _ in range(n):
    a, b = input().split('.')
    if b in file_dict:
        file_dict[b] += 1
    else:
        file_dict[b] = 1

for file, cnt in sorted(file_dict.items()):
    print(file, cnt)