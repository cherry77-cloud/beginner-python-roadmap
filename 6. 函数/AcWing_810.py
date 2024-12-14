def i_abs(x: int) -> int:
    return x if x >= 0 else -x


if __name__ == "__main__":
    x = int(input())
    print(i_abs(x))
