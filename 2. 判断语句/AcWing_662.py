a, b = map(float, input().split())

if a * b == 0:
    if a == 0 and b == 0:
        print("Origem")
    elif a != 0 and b == 0:
        print("Eixo X")
    else:
        print("Eixo Y")
else:
    if a > 0 and b > 0:
        print("Q1")
    elif a < 0 and b > 0:
        print("Q2")
    elif a < 0 and b < 0:
        print("Q3")
    else:
        print("Q4")
