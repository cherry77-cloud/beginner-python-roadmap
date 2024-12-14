l = int(input())
op = input()

a = []
for i in range(12):
    row = list(map(float, input().split()))
    a.append(row)

s = 0
for j in range(12):
    s += a[l][j]

if op == 'M':
    print("%.1f" % (s / 12))
else:
    print("%.1f" % (s))
