n = int(input())
n_stars = n
n_tabs_edge = 0
n_tabs_btw = 0
for i in range(n):
    for j in range(n_tabs_edge):
        print(end='\t')
    for j in range(n_stars):
        print('*', end='\t')
    for j in range(n_tabs_btw):
        print(end='\t')
    if i > 0 and i < n//2:
        for j in range(n_stars):
            print('*', end='\t')
    if i < n//2:
        n_stars = 1
        n_tabs_edge += 1
        n_tabs_btw = n - 2 - (2 * n_tabs_edge)
    else:
        n_stars += 2
        n_tabs_edge -= 1
        n_tabs_btw = 0
    print()