n =  int(input())
for i in range(n):
    for j in range(n):
        if (i < n//2 and j > n//2 and j < n-1) or (i > 0 and i < n//2 and j < n//2) or (i > n//2 and j > 0 and j < n//2) or (i > n//2 and i < n-1 and j > n//2):
            print(end='\t')
        else:
            print('*', end='\t')
    print()