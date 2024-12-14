k = float(input())

s1 = input()
s2 = input()
cnt = 0

for c1, c2 in zip(s1, s2):
    if c1 == c2:
        cnt += 1

if cnt / len(s1) >= k:
    print("yes")
else:
    print("no")
