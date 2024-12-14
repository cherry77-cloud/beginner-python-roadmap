n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    s = 0
    for i in range(x + 1, y):
        if i % 2 == 1:
            s += i
    print(s)
