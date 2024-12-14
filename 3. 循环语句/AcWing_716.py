idx = 1
i_max = 0

for i in range(100):
    x = int(input())
    if x > i_max:
        i_max = x
        idx = i + 1

print(i_max)
print(idx)
