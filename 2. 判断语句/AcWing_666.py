a, b, c = map(float, input().split())

a1 = max(a, b, c)
c1 = min(a, b, c)
b1 = a + b + c - a1 - c1


if c1 + b1 <= a1:
    print("NAO FORMA TRIANGULO")
else:
    if a1 ** 2 == b1 ** 2 + c1 ** 2:
        print("TRIANGULO RETANGULO")
    if a1 ** 2 > b1 ** 2 + c1 ** 2:
        print("TRIANGULO OBTUSANGULO")
    if a1 ** 2 < b1 ** 2 + c1 ** 2:
        print("TRIANGULO ACUTANGULO")
    if a1 == b1 and a1 == c1:
        print("TRIANGULO EQUILATERO")
    if (a1 == b1 and a1 > c1) or (a1 > b1 and b1 == c1):
        print("TRIANGULO ISOSCELES")
