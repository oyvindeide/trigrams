from collections import defaultdict


def tokenize(string):
    result = ""
    for char in string.lower():
        if char.isspace():
            if result and result[-1] in '>)}.,:;"':
                result = result[:-1]
            if result and result[0] in '(<{"':
                result = result[1:]
            if result:
                yield result
            result = ""
        else:
            result += char


def get_word_trigram(input_str: str):
    tokens = list(tokenize(input_str))
    word_trigram = defaultdict(set)
    for word_1, word_2, word_3 in zip(tokens, tokens[1:], tokens[2:]):
        word_trigram[word_1, word_2].add(word_3)
    return word_trigram
