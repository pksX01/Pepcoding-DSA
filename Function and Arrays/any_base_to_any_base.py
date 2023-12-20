n = int(input())
b1 = int(input())
b2 = int(input())

def AnyToDec(n, b):
    convertedNum = 0
    count = 0
    while n > 0:
        rem = n % 10
        n //= 10
        convertedNum += rem * (b ** count)
        count += 1
    return convertedNum

def DecToAny(n, b):
    convertedNum = 0
    count = 0
    while n > 0 :
        rem = n % b
        n //= b
        convertedNum += rem * (10 ** count)
        count += 1
    return convertedNum

def AnyToAny(n, b1, b2):
    decimalNum = AnyToDec(n,b1)
    finalConvertedNum = DecToAny(decimalNum, b2)
    return finalConvertedNum

if __name__ == '__main__':
    print(AnyToAny(n,b1,b2))