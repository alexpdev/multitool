import os
import sys
import json

class Words:
    all_words = json.load(open("assets/allWords.json"))
    words_extended = json.load(open("assets/words.json"))

def sanatize(input):
    clean = "".join(list(map(lambda x:" " if not x.isalpha() else x,input)))
    return clean.upper().split(" ")

def show(output):
    sys.stdout.write("Results: ")
    space = max([len(i) for i in output])
    try:
        size = os.get_terminal_size().columns
    except:
        size = 80
    space = space + 1 + len(str(len(output))) + 2
    cols, counter = size // space, 0
    print(output)
    while counter < len(output):
        line = ""
        if len(output) - counter < cols:
            cols = len(output) - counter
        for i in range(cols):
            word = output[counter].ljust(space, " ")
            phrase = f"{str(i).rjust(3, '0')}. {word}  "
            line += phrase
            counter += 1
        print(line)
    return True

def contains(args):
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
    output = []
    inp = "".join(sanatize(args.val))
    count = -1 if not count else int(count)
    for _, word in enumerate(Words.all_words):
        if not count: break
        if args.length and len(word) != int(args.length):
            continue
        if word.startswith(inp):
            output.append(word)
            count -= 1
    if output:
        return show()
    return True

def end(args):
    output = []
    inp = "".join(sanatize(args.val))
    count = -1 if not count else int(args.count)
    for _, word in enumerate(Words.all_words):
        if not count: break
        if args.length and len(word) != int(args.length):
            continue
        if word.endswith(inp) == len(inp):
            output.append(word)
            count -= 1
    if output:
        return show()
    return True

def binprint(args):
    value = int(args.value)
    print(bin(value)[2:])

def synonyms(args):
    pass
