a, b, c = map(int, input().split())

i_min = min(a, b, c)
i_max = max(a, b, c)
i_mid = a + b + c - i_min - i_max

print(i_min)
print(i_mid)
print(i_max)

print("")

print(a)
print(b)
print(c)
