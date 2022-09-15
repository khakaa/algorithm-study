for _ in range(int(input())):
    user_dict = {}
    res = 1

    for _ in range(int(input())):
        user_item, user_category = input().split()
        if user_category not in user_dict:
            user_dict[user_category] = 1
        else:
            user_dict[user_category] += 1

    for key in user_dict.keys():
        res *= (user_dict[key] + 1)
        
    print(res - 1)