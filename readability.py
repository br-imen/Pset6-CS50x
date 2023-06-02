from cs50 import get_string


def main():
    input = get_string("text: ")
    letters = count_letters(input)
    print(letters)
    words = count_words(input)
    print(words)
    sentence = count_sentence(input)
    print(sentence)
    index = round(count_index(letters, words, sentence))
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")

# count letters


def count_letters(input):
    l = 0
    for i in input:
        if i.isalpha() == True:
            l += 1

    return l

# count words


def count_words(input):
    w = 1
    for i in input:
        if i.isspace():
            w += 1
    return w

# count sentence


def count_sentence(input):
    s = 0
    for i in input:
        if i in ['.', '!', '?']:
            s += 1
    return s

# count index


def count_index(letters, words, sentence):
    L = letters / words * 100
    S = sentence / words * 100
    index = (0.0588 * L) - (0.296 * S) - 15.8
    return index


main()