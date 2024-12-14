n, m = map(int, input().split())

idx = 0
for i in range(1, n + 1):
    cir = 1
    for j in range(0, m):
        idx += 1
        cir += 1
        if cir <= m:
            print(idx, end=' ')
        else:
            print("PUM")
