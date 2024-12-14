def add(x: float, y: float) -> float:
    return x + y


if __name__ == "__main__":
    x, y = map(float, input().split())
    print("%.2f" % (add(x, y)))
