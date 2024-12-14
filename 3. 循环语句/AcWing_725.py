T = int(input())

prefect = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]

for i in range(T):
    x = int(input())
    if x in prefect:
        print("%d is perfect" % x)
    else:
        print("%d is not perfect" % x)
