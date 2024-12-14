def find_longest_word(sentence):
    sentence = sentence.rstrip('.')
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word


if  __name__ == "__main__":
    s = input()
    print(find_longest_word(s))
