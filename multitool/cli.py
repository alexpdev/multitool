import argparse
import sys

from multitool.runner import binprint, contains, synonyms


def execute(args=None):
    """
    Operate the main function for program.
    """
    if not args:
        args = sys.argv

    if len(args) <= 1:
        args.append("-h")

    parser = argparse.ArgumentParser(
        "multitool", description="Multitool CLI", prefix_chars="-"
    )
    parsers = parser.add_subparsers()
    binparser = parsers.add_parser("bin", help="Convert integers to binary")
    binparser.add_argument("value", help="Integer to convert", action="store")
    binparser.set_defaults(func=binprint)
    synparse = parsers.add_parser("syn", help="get synonyms for commong words")
    synparse.add_argument(
        "word", help="Show Synonyms for word", action="store", metavar="<word>"
    )
    synparse.set_defaults(func=synonyms)
    containsparser = parsers.add_parser(
        "contains", help="Show words that contain <text>."
    )

    containsparser.add_argument(
        "--start",
        help="Show words that start with <text>",
        dest="start",
        metavar="<text>",
        action="store",
    )
    containsparser.add_argument(
        "--end",
        help="Show words that end with <text>",
        dest="end",
        metavar="<text>",
        action="store",
    )
    containsparser.add_argument(
        "-l",
        "--length",
        help="number <n> of characters in word",
        dest="length",
        metavar="<n>",
        action="store",
    )
    containsparser.set_defaults(func=contains)

    namespace = parser.parse_args(args[1:])
    if namespace:
        print(namespace)
        namespace.func(namespace)
    return
