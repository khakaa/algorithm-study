s = input()
user_data = []

for i in range(len(s)):
    for j in range(i, len(s)):
        user_data.append(s[i:j+1])

print(len(set(user_data)))