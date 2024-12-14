def reverse_words_order(sentence):
    words = sentence.split()  # 将句子分割成单词列表
    reversed_words = words[::-1]  # 反转单词列表
    reversed_sentence = ' '.join(reversed_words)  # 重新连接单词，以单个空格分隔
    return reversed_sentence


if __name__ == "__main__":
    s = input()
    print(reverse_words_order(s))
