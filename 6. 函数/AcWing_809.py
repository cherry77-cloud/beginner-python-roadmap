import math

def lcm(x: int, y: int) -> int:
    return x * y // math.gcd(x, y)


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(lcm(x, y))
