fib = [None] * 50

fib[0] = 0
fib[1] = 1
for i in range(2, 50):
    fib[i] = fib[i - 1] + fib[i - 2]

n = int(input())
for i in range(n):
    print(fib[i], end=' ')
