import pytest
from trigrams.trigram import parse_iter, get_word_trigram


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
