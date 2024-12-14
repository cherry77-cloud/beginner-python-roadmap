n = int(input())

hour, remain = divmod(n, 3600)
minute, second = divmod(remain, 60)

print("%d:%d:%d" %(hour, minute, second))
