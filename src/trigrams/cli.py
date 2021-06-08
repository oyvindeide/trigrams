import argparse
from pathlib import Path

from trigrams.trigram import get_word_trigram


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

    result = get_word_trigram(input_data)
    for key, val in result.items():
        print(f"{key} => {val}")
