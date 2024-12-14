def two_adic_valuation(n):
    count = 0
    current = 2 * n
    while current % 2 == 0:
        count += 1
        current //= 2
    return count


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(two_adic_valuation(k))
