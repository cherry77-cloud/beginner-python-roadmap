def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
  
n = int(input())
for i in range(n):
    for j in range(n):
        if manhattan_distance(i, j, n // 2, n // 2) <= n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print("")
