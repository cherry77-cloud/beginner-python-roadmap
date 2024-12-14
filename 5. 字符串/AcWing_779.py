def longest_common_suffix(strs):
    if not strs:  return ""
    reversed_strs = [''.join(reversed(s)) for s in strs]
    shortest = min(reversed_strs, key=len)
    for i in range(len(shortest)):
        if any(s[i] != shortest[i] for s in reversed_strs):
            return shortest[:i][::-1]
    return shortest[::-1]


if __name__ == "__main__":
    while True:
        N = int(input())
        if N == 0:
            break
        strs = [input() for _ in range(N)]
        print(longest_common_suffix(strs))
