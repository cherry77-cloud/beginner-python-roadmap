a = float(input())

if 0 <= a <= 2000:
    print("Isento")
elif 2000 < a <= 3000:
    print("R$ %.2f" % ((a - 2000) * 0.08))
elif 3000 < a <= 4500:
    tax = 80 + (a - 3000) * 0.18
    print("R$ %.2f" % tax)
else:
    tax = 80 + 1500 * 0.18 + (a - 4500) * 0.28
    print("R$ %.2f" % tax)
