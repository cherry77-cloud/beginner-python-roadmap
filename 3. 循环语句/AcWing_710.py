n = int(input())

n -= 2

for i in range(6):
    if n % 2 == 0:
        print(n + 1 + 2)
    else:
        print(n + 2)
    n += 2
