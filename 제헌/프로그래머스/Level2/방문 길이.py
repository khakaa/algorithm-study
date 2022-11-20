def solution(dirs):
    answer = 0
    user_x = 0; user_y = 0;
    visited = set()
    
    for d in dirs:
        if d == 'U' and user_y < 5:
            visited.add(((user_x, user_y), (user_x, user_y+1)))
            user_y += 1
        
        elif d == 'D' and -5 < user_y:
            visited.add(((user_x, user_y-1), (user_x, user_y)))
            user_y -= 1
            
        elif d == 'R' and user_x < 5:
            visited.add(((user_x, user_y), (user_x+1, user_y)))
            user_x += 1
            
        elif d == 'L' and -5 < user_x:
            visited.add(((user_x-1, user_y), (user_x, user_y)))
            user_x -= 1
            
    return len(visited)