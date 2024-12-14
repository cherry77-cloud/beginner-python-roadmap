import random

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # 将n-1写成2^r * d的形式
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # 进行k轮测试
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

t = int(input())
for i in range(t):
    x = int(input())
    if miller_rabin(x, 5):
        print("%d is prime" % x)
    else:
        print("%d is not prime" % x)
