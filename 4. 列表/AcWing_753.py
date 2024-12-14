while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        for j in range(n):
            t = min(i, j, n - i - 1, n - j - 1)
            print(t + 1, end=' ')
        print()

    print()
