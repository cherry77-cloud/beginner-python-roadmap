def find_substrings(s):
    substr_count = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr in substr_count:
                substr_count[substr] += 1
            else:
                substr_count[substr] = 1
    frequent_substrings = {k: v for k, v in substr_count.items() if v > 1}
    return frequent_substrings


# 读取输入直到EOF
while True:
    try:
        s = input()
        result = find_substrings(s)
        for substr in sorted(result):
            print(f"{substr} {result[substr]}")
    except EOFError:
        break
