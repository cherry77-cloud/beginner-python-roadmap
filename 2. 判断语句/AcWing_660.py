n, m = map(int, input().split())

cnt = [-1, 4.00, 4.50, 5.00, 2.00, 1.50]

print("Total: R$ %.2f" % (cnt[n] * m))
