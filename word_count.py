# This program prints the number of times each word occurs in a sentence
words_dict = {}


def word_count(string):
    string = string.lower()
    words = string.split()
    for word in words:
        words_dict.update({word: words.count(word)})
    return words_dict


sentence = str(input("Please enter a sentence: "))
print(word_count(sentence))
