while True:
    x, y = map(int, input().split())
    if x <= 0 or y <= 0:
        break
    if x > y:
        x, y = y, x
    s = 0
    for i in range(x, y + 1):
        print(i, end=' ')
        s += i
    print("Sum=%d" % s)
