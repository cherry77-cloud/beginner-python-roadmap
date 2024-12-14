def i_max(x: int, y: int) -> int:
    return x if x >= y else y

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(i_max(x, y))
