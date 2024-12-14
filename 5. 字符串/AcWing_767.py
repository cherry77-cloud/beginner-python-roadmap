def encrypt_string(s):
    encrypted = ""
    for char in s:
        if 'a' <= char <= 'y' or 'A' <= char <= 'Y':
            encrypted += chr(ord(char) + 1)
        elif char == 'z':
            encrypted += 'a'
        elif char == 'Z':
            encrypted += 'A'
        else:
            encrypted += char
    return encrypted


if __name__ == "__main__":
    s = input()
    print(encrypt_string(s))
