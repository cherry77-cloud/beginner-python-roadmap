n = int(input())
count = dict()
a = list(map(int, input().split()))

for x in a:
    if x not in count:
        count[x] = 0
    count[x] += 1
    print(count[x], end=' ')
