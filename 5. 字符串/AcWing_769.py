def replace_char_with_hash(s, char_to_replace):
    return s.replace(char_to_replace, '#')

s = input()
op = input()
print(replace_char_with_hash(s, op))
