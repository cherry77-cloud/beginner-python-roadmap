def longest_consecutive_char(s):
    max_char = s[0]
    max_count = 1
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_char = s[i]
        else:
            current_count = 1
    return max_char, max_count


n = int(input())

for _ in range(n):
    s = input()
    max_c, max_t = longest_consecutive_char(s)
    print("%c %d" % (max_c, max_t))
