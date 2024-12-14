op = input()

a = []

for _ in range(12):
    b = list(map(float, input().split()))
    a.append(b)

s = 0
for i in range(12):
    for j in range(12):
        if j <= 4 and j + 1 <= i and i + j <= 10:
            s += a[i][j]

if op == "M":
    print("%.1f" % (s / 30))
else:
    print("%.1f" % (s))
