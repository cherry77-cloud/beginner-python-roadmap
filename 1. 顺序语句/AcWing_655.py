n = int(input())

years, remain = divmod(n, 365)
months, days = divmod(remain, 30)

print("%d ano(s)" % years)
print("%d mes(es)" % months)
print("%d dia(s)" % days)
