import json
import os
import sys


class Words:
    """
    Namespace containing reference documents for gathering data.
    """

    all_words = json.load(open("assets/Words_Length.json"))
    word_frequencies = json.load(open("assets/Words_Frequency.json"))
    synonyms = json.load(open("assets/Synonyms.json"))


def sanatize(input):
    """
    Convert input command line arguments into format contained by documents.
    """
    return input.upper()


def show(output):
    """
    Format the output to show user on console screen.
    """
    sys.stdout.write("Results: ")
    space = max([len(i) for i in output])
    try:
        size = os.get_terminal_size().columns
    except:
        size = 80
    space = space + 1 + len(str(len(output))) + 2
    cols, counter = size // space, 0
    while counter < len(output):
        line = ""
        if len(output) - counter < cols:
            cols = len(output) - counter
        for i in range(cols):
            word = output[counter].ljust(space, " ")
            phrase = f"{str(i).rjust(3, '0')}. {word}  "
            line += phrase
            counter += 1
    return True


def contains(args):
    """
    Check if words exist that contain the partial word within the word.
    """
    if args.start or args.end:
        if args.start:
            return start(args)
        return end(args)
    else:
        output = []
        inp = sanatize(args.val)
        count = -1 if not count else int(count)
        for _, word in enumerate(Words.all_words):
            if count == 0:
                break
            if args.length and len(word) != int(args.length):
                continue
            if len([part for part in inp if part in word]) == len(inp):
                output.append(word)
                count -= 1
        if output:
            return show()
    return True


def start(args):
    """
    Check contains but only from the start of the word.
    """
    output = []
    inp = "".join(sanatize(args.val))
    count = -1 if not count else int(count)
    for _, word in enumerate(Words.all_words):
        if not count:
            break
        if args.length and len(word) != int(args.length):
            continue
        if word.startswith(inp):
            output.append(word)
            count -= 1
    if output:
        return show()
    return True


def end(args):
    """
    Check contains but only at the end of the word.
    """
    output = []
    inp = "".join(sanatize(args.val))
    count = -1 if not count else int(args.count)
    for _, word in enumerate(Words.all_words):
        if not count:
            break
        if args.length and len(word) != int(args.length):
            continue
        if word.endswith(inp) == len(inp):
            output.append(word)
            count -= 1
    if output:
        return show()
    return True


def binprint(args):
    """
    Return binary representation of decimal digit.
    """
    value = int(args.value)
    print(bin(value)[2:])
    return value


def synonyms(args):
    """
    Return Synonyms for the inputed word.
    """
    w = args.word.lower()
    collection = []
    for entry in Words.synonyms:
        if w in entry["word"]:
            collection.append(entry)
    reg = {}
    for entry in collection:
        if entry["word"] in reg:
            reg[entry["word"]].extend(entry["synonyms"])
        else:
            reg[entry["word"]] = entry["synonyms"]

    for k, v in reg.items():
        output = f":{k} \n"
        for syn in v:
            output += f"\t {syn} \n"
        sys.stdout.write(output)
    return output
