n = int(input())
print(n)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    num, remain = divmod(n, nota)
    n = remain
    print("%d nota(s) de R$ %d,00" % (num, nota))
