def copy_and_print(a: list, b: list, size: int) -> None:
    for i in range(size):
        b[i] = a[i]


if __name__ == "__main__":
    n, m, size = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    copy_and_print(a, b, size)
    for x in b:
        print(x, end=' ')
