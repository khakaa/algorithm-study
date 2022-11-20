def solution(citations):
    citations.sort(reverse=True)
    for idx,i in enumerate(citations):
        if idx>=i:
            print(idx)
            return idx
    print(len(citations))
    return len(citations)

if __name__ == "__main__":
    solution([3,0,6,1,5])