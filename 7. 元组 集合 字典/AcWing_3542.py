n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
for x in map(int, input().split()):
    print("YES" if x in s1 else "NO")
