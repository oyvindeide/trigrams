import random

import pytest
from trigrams.trigram import parse_iter, get_word_trigram, create_text


def test_word_trigram():
    example_string = "I wish I may I wish I might"
    result = {
        "I wish": ["I", "I"],
        "wish I": ["may", "might"],
        "may I": ["wish"],
        "I may": ["I"],
    }

    assert get_word_trigram(example_string) == result


@pytest.mark.parametrize(
    "valid_input, expected_result",
    [("abc", [["a", "b", "c"]]), (["a", "b", "c"], [["a", "b", "c"]])],
)
def test_parser(valid_input, expected_result):
    assert parse_iter(valid_input) == expected_result


def test_create_text():
    input_data = {
        "I wish": ["I", "I"],
        "wish I": ["may", "might"],
        "may I": ["wish"],
        "I may": ["I"],
    }

    random.seed(1234)
    assert create_text(2, input_data) == "I may I wish"
