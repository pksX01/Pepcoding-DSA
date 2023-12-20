b = int(input())
n1 = int(input())
n2 = int(input())

def addAnyBase(b, n1, n2):
    sum = 0
    count = 0
    carry = 0
    while (n1 > 0 or n2 > 0 or carry > 0):
        digit1 = n1 % 10
        n1 //= 10
        digit2 = n2 % 10
        n2 //= 10
        digitSum = carry + digit1 + digit2
        carry = digitSum // b
        digit = digitSum % b
        sum += digit * (10 ** count)
        count += 1
    return sum

if __name__ == '__main__':
    print(addAnyBase(b,n1,n2))