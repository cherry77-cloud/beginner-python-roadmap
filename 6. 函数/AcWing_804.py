def fact(n: int) -> int:
    if n == 1:  return 1
    return fact(n - 1) * n


if __name__ == "__main__":
    n = int(input())
    print(fact(n)
