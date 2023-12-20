n = int(input())
b = int(input())

def AnyToDec(n, b):
    decimalNum = 0
    count = 0
    while(n > 0):
        rem = n % 10
        n //= 10
        decimalNum += rem * (b ** count)
        count += 1
    return decimalNum

if __name__ == '__main__':
    print(AnyToDec(n,b))
