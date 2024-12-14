def replace_word(s, old_word, new_word):
    words = s.split()  # 将字符串按空格分割成单词列表
    new_words = [new_word if word == old_word else word for word in words]
    return ' '.join(new_words)  # 使用空格重新连接单词


if __name__ == "__main__":
    words = input()
    old_word = input()
    new_word = input()
    print(replace_word(words, old_word, new_word))
