T = int(input())
all_number = [0,1,2,3,4,5,6,7,8,9]
tc = []
ans = []
for _ in range(T):
    tc.append(int(input()))

for n in tc:
    count_sheep = []
    i = 1
    while count_sheep != all_number:
        sheep_number = n * i
        ans_number = n * i
        while sheep_number != 0:
            count_sheep.append(sheep_number % 10)
            sheep_number //= 10
        i += 1
        count_sheep.sort()
        count_sheep = list(set(count_sheep))

    ans.append(ans_number)

for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')