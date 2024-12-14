n = int(input())

city_table = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

if city_table.get(n) is not None:
    print(city_table[n])
else:
    print("DDD nao cadastrado")
