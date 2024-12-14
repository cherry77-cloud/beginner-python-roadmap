def fib(x: int) -> int:
    if x <= 2:
        return 1
    return fib(x - 1) + fib(x - 2)


if __name__ == "__main__":
    n = int(input())
    print(fib(n))
