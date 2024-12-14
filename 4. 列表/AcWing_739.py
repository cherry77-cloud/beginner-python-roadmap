idx = 0

for i in range(100):
    x = float(input())
    if x <= 10:
        print("A[%d] = %.1f" % (idx, x))
    idx += 1
