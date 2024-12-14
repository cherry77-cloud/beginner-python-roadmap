def compare_strings_ignore_case(str1, str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    if str1_lower < str2_lower:
        return -1
    elif str1_lower > str2_lower:
        return 1
    else:
        return 0

s1 = input()
s2 = input()

if compare_strings_ignore_case(s1, s2) == -1:
    print("<")
elif compare_strings_ignore_case(s1, s2) == 0:
    print("=")
else:
    print(">")
