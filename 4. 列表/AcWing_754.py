while True:
    n = int(input())
    if n == 0:
        break
    a = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = 1
            if j > i:
                a[i][j] = j - i + 1
            if j < i:
                a[i][j] = i - j + 1

    for k in range(n):
        for v in range(n):
            print(a[k][v], end=' ')
        print()
    print()
