b = int(input())
n1 = int(input())
n2 = int(input())

def any_base_sub(b, n1, n2):
    borrow = 0
    result = 0
    count = 0
    while (n1 > 0 or n2 > 0):
        digit1 = n1 % 10
        n1 //= 10
        digit2 = n2 % 10
        n2 //= 10
        diff = digit2 - digit1 - borrow
        borrow = 0
        if diff < 0:
            diff = b + diff
            borrow = 1
        result += diff * (10 ** count)
        count += 1
    return result

if __name__ == '__main__':
    print(any_base_sub(b,n1,n2))
