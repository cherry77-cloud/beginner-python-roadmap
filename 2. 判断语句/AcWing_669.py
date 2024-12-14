def calculate_salary_adjustment(n):
    if 0 <= n <= 400:
        percentual = 0.15
    elif 400 < n <= 800:
        percentual = 0.12
    elif 800 < n <= 1200:
        percentual = 0.10
    elif 1200 < n <= 2000:
        percentual = 0.07
    else:
        percentual = 0.04

    salario = n * (1 + percentual)
    ganho = n * percentual
    return salario, ganho, int(percentual * 100)


n = float(input())
salario, ganho, percentual = calculate_salary_adjustment(n)


print("Novo salario: %.2f" % salario)
print("Reajuste ganho: %.2f" % ganho)
print("Em percentual: %d %%" % percentual)
