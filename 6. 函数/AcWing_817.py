def get_unique_count(a: list, n: int) -> int:
    s1 = set()
    for i in range(n):
        s1.add(a[i])
    return len(s1)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(get_unique_count(a, n))
