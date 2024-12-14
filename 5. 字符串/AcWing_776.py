def is_rotation(s1, s2):
    if len(s2) > len(s1):
        return False
    return s2 in (s1 + s1)


if __name__ == "__main__":
    s1, s2 = input().split()
    if is_rotation(s1, s2) or is_rotation(s2, s1):
        print("true")
    else:
        print("false")
