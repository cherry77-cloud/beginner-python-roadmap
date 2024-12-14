fib = [0] * 61

fib[0] = 0
fib[1] = 1

for i in range(2, 61):
    fib[i] = fib[i - 1] + fib[i - 2]

n = int(input())

for _ in range(n):
    idx = int(input())
    print("Fib(%d) = %d" % (idx, fib[idx]))
