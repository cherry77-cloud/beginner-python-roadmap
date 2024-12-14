n = int(input())
s = set(map(int, input().split()))
print(sum(1 for x in s if x > 0))
