def reverse(a: list, size: int) -> None:
    i, j = 0, size - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    n, size = map(int, input().split())
    a = list(map(int, input().split()))
    reverse(a, size)
    for x in a:
        print(x, end=' ')
