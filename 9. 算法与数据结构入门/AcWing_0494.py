cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def get(x: int) -> int:
    return sum(cnt[int(digit)] for digit in str(x))

tables = [get(i) for i in range(2000)]
n = int(input())
ans = 0

for i in range(1000):
    for j in range(1000):
        if tables[i] + tables[j] + 4 + tables[i + j] == n:
            ans += 1

print(ans)
