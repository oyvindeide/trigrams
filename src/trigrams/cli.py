import argparse
from pathlib import Path

from trigrams.trigram import get_word_trigram, create_text


def _is_valid_file(arg):
    if Path(arg).exists():
        return arg
    raise argparse.ArgumentTypeError("{} is not an existing file!".format(arg))


def _parser():

    parser = argparse.ArgumentParser(description="trigrams")

    parser.add_argument(
        "-i",
        "--input_file",
        help="Pure text file",
        type=_is_valid_file,
        required=True,
    )

    return parser


def main():
    parser = _parser()
    options = parser.parse_args()

    with open(options.input_file, "r") as fin:
        input_data = fin.read().replace("\n", " ")

    filtered_input = sanitize_input(input_data)

    result = get_word_trigram(filtered_input)

    print(create_text(200, result))


def sanitize_input(input_str):
    input_data = input_str.lower()

    filtered_data = ""
    for letter in input_data:
        if letter.isalpha() or letter == " ":
            filtered_data += letter
    return filtered_data
