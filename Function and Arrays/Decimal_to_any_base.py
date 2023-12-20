n = int(input())
b = int(input())

def DecToAny(n, b):
    convertedNum = 0
    count = 0
    while (n > 0):
        rem = n % b
        n //= b
        convertedNum += rem * (10 ** count)
        count += 1
    return convertedNum

if __name__ == '__main__':
    print(DecToAny(n,b))