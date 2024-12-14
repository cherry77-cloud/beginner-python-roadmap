def i_sum(l: int, r: int) -> int:
    return (l + r) * (r - l + 1) // 2


if __name__ == "__main__":
    l, r = map(int, input().split())
    print(i_sum(l, r))
