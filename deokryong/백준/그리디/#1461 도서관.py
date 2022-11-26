N, M = map(int,input().split())

books = list(map(int,input().split()))
books_minus = [books[i] for i in range(len(books)) if books[i] < 0]
books_plus = [books[i] for i in range(len(books)) if books[i] > 0]

if len(books_minus) == 0:
    max_minus=0
else:
    max_minus = -min(books_minus)
    books_minus.sort()

if len(books_plus) == 0:
    max_plus=0
else:
    max_plus = max(books_plus)
    books_plus.sort(reverse=True)

max_value = max_minus if max_minus > max_plus else max_plus
total = 0
while True:
    if len(books_minus)==0 and len(books_plus) ==0:
        break
    for i in range(M):
        if len(books_minus) == 0:
            break
        if i == 0:
            total -= (books_minus.pop(0)*2)
        else:
            books_minus.pop(0)
    for i in range(M):
        if len(books_plus) == 0:
            break
        if i == 0:
            total += (books_plus.pop(0)*2)
        else:
            books_plus.pop(0)

print(total-max_value)