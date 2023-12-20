n = int(input())
n_stars = n
n_tabs = 0
for i in range(n):
    for j in range(n_tabs):
        print(end='\t')
    for j in range(n_stars):
        if i > 0 and i < n//2 and j > 0 and j < n_stars-1:
            print(end='\t')
        else:
            print('*', end='\t')
    if i < n//2:
        n_stars -= 2
        n_tabs += 1
    else:
        n_stars += 2
        n_tabs -= 1
    print()