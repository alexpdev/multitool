import sys
import argparse
from multitool.runner import Runner


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
    parser.add_argument(
        "--syn",
        help="Show Synonyms for word",
        action="store",
        dest="syn",
        metavar="<word>"
    )
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
    return process_args(**vars(namespace))

def process_args(count=None, length=None, end=None,
                 contains=None, start=None, syn=None):
    runner = Runner()
    if contains:
        return runner.contains(contains, count, length)
    if syn:
        return runner.synonyms(syn, count, length)
    if start:
        return runner.start(start, count, length)
    if end:
        return runner.end(end, count, length)
