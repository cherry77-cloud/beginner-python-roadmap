while True:
    n = int(input())
    if n == 0:
        break
    a = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(n):
        for j in range(n):
            a[i][j] = 2 ** (i + j)

    for k in range(n):
        for v in range(n):
            print(a[k][v], end=' ')
        print()
    print()
