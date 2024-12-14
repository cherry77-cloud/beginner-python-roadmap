n = int(input())
s = set()
for _ in range(n):
    op, x = input().split()
    if op == "I":
        s.add(int(x))
    else:
        print("Yes" if int(x) in s else "No")
