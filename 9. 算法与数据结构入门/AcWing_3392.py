a0, a1, p, q, k = map(int, input().split())
mod = 10000

a = [0 for _ in range(k + 1)]
a[0], a[1] = a0 % mod, a1 % mod

for i in range(2, k + 1):
    a[i] = (p * a[i - 1] + q * a[i - 2]) % mod

print(a[k])
