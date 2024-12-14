def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return gcd(y, x % y)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
