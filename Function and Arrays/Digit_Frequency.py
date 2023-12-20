n = int(input())
d = int(input())
count = 0
while (n % 10 != 0):
    if d == n % 10:
        count += 1
    n //= 10
print(count)