def compute_lps(s):
    n = len(s)
    lps = [0] * n
    len_lps = 0
    i = 1
    while i < n:
        if s[i] == s[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1
        else:
            if len_lps != 0:
                len_lps = lps[len_lps - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def max_repetition(s):
    lps = compute_lps(s)
    n = len(s)
    len_lps = lps[-1]

    if len_lps == 0 or n % (n - len_lps) != 0:
        return 1
    else:
        return n // (n - len_lps)


if __name__ == "__main__":
    while True:
        s = input().strip()
        if s == ".":
            break
        print(max_repetition(s))
