def insert_substr_after_max_char(string, substr):
    max_char = max(string)
    max_index = string.index(max_char)
    new_string = string[:max_index + 1] + substr + string[max_index + 1:]
    return new_string

while True:
    try:
        s1, s2 = input().split()
        print(insert_substr_after_max_char(s1, s2))
    except ValueError:
        break
    except EOFError:
        break
