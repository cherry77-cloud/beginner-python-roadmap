op = input()

a = []
for i in range(12):
    row = list(map(float, input().split()))
    a.append(row)

s = 0
for j in range(12):
    for k in range(12):
        if k > j:
            s += a[j][k]

if op == 'M':
    print("%.1f" % (s / 66))
else:
    print("%.1f" % (s))
