N = int(input())
book = {}
answer = []

for _ in range(N):
    b = input()
    if b in book:
        book[b] += 1
    else:
        book[b] = 1

max_count = max(book.values())

for b,c in book.items():
    if max_count == c:
        answer.append(b)

answer.sort()
print(answer[0])