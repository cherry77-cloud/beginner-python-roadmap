n = int(input())

cnt1 = cnt2 = 0

for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        cnt1 += 1
    else:
        cnt2 += 1

print("%d in" % cnt1)
print("%d out" % cnt2)
