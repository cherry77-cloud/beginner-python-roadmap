col = int(input())
op = input()

a = []
for _ in range(12):
    row = list(map(float, input().split()))
    a.append(row)

s = 0
for i in range(12):
    s += a[i][col]

if op == "S":
    print("%.1f" % s)
else:
    print("%.1f" % (s / 12))
