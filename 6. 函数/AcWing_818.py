def sort_segment(a: list, l: int, r: int) -> None:
    a[l:r+1] = sorted(a[l:r+1])


if __name__ == "__main__":
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    sort_segment(a, l, r)

    for x in a:
        print(x, end=' ')
