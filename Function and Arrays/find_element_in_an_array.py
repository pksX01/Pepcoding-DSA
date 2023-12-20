if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    d = int(input())
    for index, ele in enumerate(arr):
        if ele == d:
            print(index)
            break
    else:
        print(-1)