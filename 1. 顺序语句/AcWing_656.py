money = float(input())

# 定义纸币面额
banknotes = [
    (100, "nota(s) de R$ 100.00"),
    (50, "nota(s) de R$ 50.00"),
    (20, "nota(s) de R$ 20.00"),
    (10, "nota(s) de R$ 10.00"),
    (5, "nota(s) de R$ 5.00"),
    (2, "nota(s) de R$ 2.00")
]

# 定义硬币面额
coins = [
    (1.00, "moeda(s) de R$ 1.00"),
    (0.50, "moeda(s) de R$ 0.50"),
    (0.25, "moeda(s) de R$ 0.25"),
    (0.10, "moeda(s) de R$ 0.10"),
    (0.05, "moeda(s) de R$ 0.05"),
    (0.01, "moeda(s) de R$ 0.01")
]

# 转换总金额为分，以避免浮点数精度问题
total_cents = int(round(money * 100))

# 输出纸币
print("NOTAS:")
for value, description in banknotes:
    value_in_cents = int(value * 100)
    count = total_cents // value_in_cents
    total_cents %= value_in_cents
    print(f"{count} {description}")

# 输出硬币
print("MOEDAS:")
for value, description in coins:
    value_in_cents = int(round(value * 100))
    count = total_cents // value_in_cents
    total_cents %= value_in_cents
    print(f"{count} {description}")
