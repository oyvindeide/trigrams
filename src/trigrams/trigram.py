from collections import defaultdict


def get_word_trigram(input_str: str):
    string_list = input_str.split(" ")
    trigrams = parse_iter(string_list)
    word_trigram = defaultdict(list)
    for word_1, word_2, word_3 in trigrams:
        word_trigram[word_1 + " " + word_2].append(word_3)
    return word_trigram


def parse_iter(tokens):
    if len(tokens)<=2:
        raise ValueError(f"tokens must be of length greater than 2, was {len(tokens)}")
    trigram = []
    token_1 = tokens[0]
    token_2 = tokens[1]
    for token_3 in tokens[2:]:
        trigram.append([token_1, token_2, token_3])
        token_1 = token_2
        token_2 = token_3
    return trigram
