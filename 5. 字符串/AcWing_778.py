def find_max_span(s: str, s1: str, s2: str):
    positions_s1 = [i for i in range(len(s)) if s.startswith(s1, i)]
    positions_s2 = [i for i in range(len(s)) if s.startswith(s2, i)]
    if not positions_s1 or not positions_s2:
        return -1
    max_span = max(positions_s2) - min(positions_s1) - len(s1)
    if max_span < 0:
        return -1
    else:
        return max_span


if __name__ == "__main__":
    s, s1, s2 = input().split(",")
    print(find_max_span(s, s1, s2))
