def getSpan(arr):
    max, min = 0, arr[0]
    for ele in arr:
        if ele >= max:
            max = ele
        if ele <= min:
            min = ele
    return max - min

if __name__ == '__main__':
    n = int(input())
    arr = [0]*n
    for i in range(0,n):
        arr[i] = int(input())
    print(getSpan(arr))