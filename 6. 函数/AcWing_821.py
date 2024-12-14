def foo(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return foo(n - 1) + foo(n - 2)


if __name__ == "__main__":
    n = int(input())
    print(foo(n))
