def min_flip_coins(s1: str, s2: str) -> int:
    cnt = 0
    s2 = list(s2)
    for i in range(len(s1) - 1):
        if s1[i] != s2[i]:
            cnt += 1
            s2[i] = s1[i]
            s2[i + 1] = '*' if s2[i + 1] == 'o' else 'o'
    return cnt


if __name__ == "__main__":
    init_state = input()
    target_state = input()
    print(min_flip_coins(init_state, target_state))
