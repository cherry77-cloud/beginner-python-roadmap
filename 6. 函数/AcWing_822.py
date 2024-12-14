def combination(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(combination(n + m, n))
