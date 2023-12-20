n = int(input())
for i in range(n):
    for j in range(n):
        if (j == 0 or j == n-1) or (i <= n//2 and (i == j or j == n-1-i)):
            print('*', end='\t')
        else:
            print(end='\t')
    print()