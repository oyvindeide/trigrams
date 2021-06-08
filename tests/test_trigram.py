import pytest
from trigrams.trigram import split, parse_iter, get_word_trigram


def test_split():
    assert split("") == []
    assert split("abcdef ") == ["abcdef"]
    assert split("abcdef") == ["abcdef"]
    assert split("ab cd ef") == ["ab", "cd", "ef"]
    assert split("ab, cd.- ef!!") == ["ab", "cd", "ef"]
    assert split("it's") == ["it's"]
    assert split("a b c") == ["a", "b", "c"]


def test_word_trigram():
    example_string = "I wish I may I wish I might"
    result = {
        ("I", "wish"): ["I", "I"],
        ("wish", "I"): ["may", "might"],
        ("may", "I"): ["wish"],
        ("I", "may"): ["I"],
    }

    assert get_word_trigram(example_string) == result


@pytest.mark.parametrize(
    "valid_input, expected_result",
    [("abc", [("a", "b", "c")]), (["a", "b", "c"], [("a", "b", "c")])],
)
def test_parser(valid_input, expected_result):
    assert list(parse_iter(valid_input)) == expected_result
