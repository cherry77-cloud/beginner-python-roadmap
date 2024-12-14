def print1D(a: list, size: int) -> None:
    if size > len(a):
        raise ValueError("Size is larger than the array length.")
    for i in range(size):
        print(a[i], end=' ')


if __name__ == "__main__":
    n, size = map(int, input().split())
    a = list(map(int, input().split()))
    print1D(a, size)
