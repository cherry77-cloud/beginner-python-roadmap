a, b, c, d = map(float, input().split())

media = (a * 2 + b * 3 + c * 4 + d) / 10

print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    y = float(input())
    print("Nota do exame: %.1f" % y)
    z = (media + y) / 2
    if z >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % z)
