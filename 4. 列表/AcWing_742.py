n = int(input())

a = list(map(int, input().split()))

temp, idx = 1001, -1

for i, x in enumerate(a):
    if x < temp:
        temp = x
        idx = i

print("Minimum value: %d" % temp)
print("Position: %d" % idx)
