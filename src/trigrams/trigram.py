import random
from collections import defaultdict


def get_word_trigram(input_str: str):
    string_list = input_str.split(" ")
    trigrams = parse_iter(string_list)
    word_trigram = defaultdict(list)
    for word_1, word_2, word_3 in trigrams:
        word_trigram[word_1 + " " + word_2].append(word_3)
    return word_trigram


def parse_iter(tokens):
    trigram = []
    token_1 = tokens[0]
    token_2 = tokens[1]
    for token_3 in tokens[2:]:
        trigram.append([token_1, token_2, token_3])
        token_1 = token_2
        token_2 = token_3
    return trigram


def create_text(nr_words, trigram_map, start_key="random"):
    if start_key == "random":
        key = random.choice(list(trigram_map.keys()))
    else:
        if start_key in trigram_map.keys():
            key = start_key
        else:
            raise ValueError(f"No such key {start_key}" in {trigram_map.keys()})
    result = key
    for _ in range(nr_words):
        next_word = random.choice(trigram_map[key])
        result += " " + next_word
        key = key.split(" ")[1] + " " + next_word
    return result
