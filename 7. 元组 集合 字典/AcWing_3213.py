n = int(input())

a = list(map(int, input().split()))

counts = dict()

for x in a:
    if x not in counts:
        counts[x] = 0
    counts[x] += 1

sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

for k, v in sorted_counts:
    print("%d %d" %(k, v))
