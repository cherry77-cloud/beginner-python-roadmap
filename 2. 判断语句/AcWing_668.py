a, b, c, d = map(int, input().split())

t1 = a * 60 + b
t2 = c * 60 + d

if t1 < t2:
    hour, minute = divmod(t2 - t1, 60)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hour, minute))
elif t1 == t2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    hour, minute = divmod(t2 - t1 + 1440, 60)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hour, minute))
