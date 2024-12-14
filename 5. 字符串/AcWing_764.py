def transform_string(s):
    ans = ""
    n = len(s)
    for i in range(n):
        next_char = s[(i + 1) % n]
        ans += chr(ord(s[i]) + ord(next_char))
    return ans

a = input()
print(transform_string(a))
