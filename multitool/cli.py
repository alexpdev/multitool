import sys
import argparse
from multitool.runner import binprint


def execute(args=None):
    if not args:
        args = sys.argv

    if len(args) <= 1:
        args.append("-h")

    parser = argparse.ArgumentParser(
        "multitool",
        description="Multitool CLI",
        prefix_chars="-"
    )
    parsers = parser.add_subparsers()
    binparser = parsers.add_parser("bin", help="Convert integers to binary")
    binparser.add_argument("value", help="Integer to convert", action="store")
    binparser.set_defaults(func=binprint)
    synparse = parsers.add_parser(
        "syn", alias="synonym"
    )
    synparse.add_arguement(
        "word",
        help="Show Synonyms for word",
        action="store",
        metavar="<word>"
    )
    synparse.set_defaults()
    parser.add_argument(
        "--start",
        help="Show words that start with <text>",
        dest="start",
        metavar="<text>",
        action="store"
    )
    parser.add_argument(
        "--contains",
        "--in",
        help="Show words that countain <text>",
        action="store",
        dest="contains",
        metavar="<text>"
    )
    parser.add_argument(
        "--end",
        help="Show words that end with <text>",
        dest="end",
        metavar="<text>",
        action="store"
    )
    parser.add_argument(
        "-l",
        "--length",
        help="number <n> of characters in word",
        dest="length",
        metavar="<n>",
        action="store"
    )
    parser.add_argument(
        "-c",
        "--count",
        dest="count",
        help="maximum number of results in output. (default=50)",
        metavar="<n>",
        action="store"
    )

    namespace = parser.parse_args(args[1:])
    if namespace:
        print(namespace)
        namespace.func(namespace)
    return
