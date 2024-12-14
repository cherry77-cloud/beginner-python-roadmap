s = input()
cnt = sum('a' <= x <= 'z' for x in set(s))
print("even" if cnt % 2 == 0 else "odd")
