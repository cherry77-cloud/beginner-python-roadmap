def remove_extra_spaces(s):
    words = s.split()  # 将字符串按空格分割
    return ' '.join(words)  # 使用单个空格重新连接单词


if __name__ == "__main__":
    s = input()
    print(remove_extra_spaces(s))
