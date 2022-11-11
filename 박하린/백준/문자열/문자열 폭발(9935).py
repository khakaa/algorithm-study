input_str = input().strip()
pattern = input().strip()
stack = []

for i in range(len(input_str)):
    stack.append(input_str[i])

    if len(stack) >= len(pattern):
        tmp = ''.join(stack[-len(pattern):])

        if tmp == pattern:
            cnt = 0
            while cnt < len(pattern):
                stack.pop()
                cnt += 1

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))