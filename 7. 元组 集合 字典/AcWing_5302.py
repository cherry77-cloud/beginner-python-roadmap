n = int(input())

str_table = dict()

for _ in range(n):
    k, v = input().split()
    v = int(v)
    str_table[k] = v

m = int(input())

for _ in range(m):
    op = input()
    if op not in str_table:
        print("-1")
    else:
        print(str_table.get(op))
