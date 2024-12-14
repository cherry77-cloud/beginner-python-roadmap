def select_sort(q: list) -> list:
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            if q[j] < q[i]:
                q[i], q[j] = q[j], q[i]


if __name__ == "__main__":
    n = int(input())
    q = list(map(int, input().split()))
    select_sort(q)
    for x in q:
        print(x, end=' ')
