import re
from collections import defaultdict


def split(input_str):
    words = []
    start_index = 0
    index = 0
    input_str += " "
    while index < len(input_str):
        char = input_str[index]
        if char not in "'" and not char.isalnum():
            word = input_str[start_index:index]
            if word:
                words.append(word)
            for start_index, char in enumerate(input_str[index:]):
                if char.isalnum():
                    break
            else:
                break
            start_index += index
            index = start_index
        index += 1
    return words


def get_word_trigram(input_str: str):
    string_list = split(input_str)
    word_trigram = defaultdict(list)
    for word_1, word_2, word_3 in parse_iter(string_list):
        word_trigram[(word_1, word_2)].append(word_3)
    return word_trigram


def parse_iter(tokens):
    token_1 = tokens[0]
    token_2 = tokens[1]
    for token_3 in tokens[2:]:
        yield token_1, token_2, token_3
        token_1 = token_2
        token_2 = token_3
