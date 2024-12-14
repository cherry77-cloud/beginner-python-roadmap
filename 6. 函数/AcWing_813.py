def print2D(a: list, row: int, col: int) -> None:
    for i in range(row):
        for j in range(col):
            print(a[i][j], end=' ')
        print()  # 每行结束后打印换行符


if __name__ == "__main__":
    row, col = map(int, input().split())
    a = []
    for _ in range(row):
        a.append(list(map(int, input().split())))
    print2D(a, row, col)
