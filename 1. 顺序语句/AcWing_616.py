import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("%.4f" % dis)
