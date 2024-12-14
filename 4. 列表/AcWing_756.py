n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

res = [[0 for _ in range(m)] for _ in range(n)]

x, y, d = 0, 0, 0

for i in range(1, n * m + 1):
    res[x][y] = i
    a, b = x + dx[d], y + dy[d]
    if a < 0 or a >= n or b < 0 or b >= m or res[a][b]:
        d = (d + 1) % 4
        a, b = x + dx[d], y + dy[d]
    x, y = a, b

for k in range(n):
    for v in range(m):
        print(res[k][v], end=' ')
    print()
