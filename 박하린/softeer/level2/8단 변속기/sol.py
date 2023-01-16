trans = list(map(int, input().split(' ')))
ans = ""
if trans[0] == 1:
    ans = "ascending"
elif trans[0] == 8:
    ans = "descending"
else:
    ans = "mixed"

for i in range(1, len(trans)):
    if trans[i-1] + 1 == trans[i]:
        ans = "ascending"
    elif trans[i-1] - 1 == trans[i]:
        ans = "descending"
    else:
        ans = "mixed"
        break
print(ans)