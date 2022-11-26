S = list(input())
T = list(input())

while True:
    if len(S) == len(T):
        if S == T:
            print(1)
        else:
            print(0)
        break
    if T[-1] == 'A':
        T.pop(-1)
    elif T[-1] == 'B':
        T.pop(-1)
        T.reverse()
    print(T)