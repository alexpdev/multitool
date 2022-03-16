import os
import sys
import json

class Runner:

    def __init__(self):
        self.all_words = json.load(open("assets/allWords.json"))
        self.words_extended = json.load(open("assets/words.json"))
        self.output = []

    def sanatize(self, input):
        clean = "".join(list(map(lambda x:" " if not x.isalpha() else x,input)))
        return clean.upper().split(" ")

    def show(self):
        sys.stdout.write("Results: ")
        space = max([len(i) for i in self.output])
        try:
            size = os.get_terminal_size().columns
        except:
            size = 80
        space = space + 1 + len(str(len(self.output))) + 2
        cols, counter = size // space, 0
        print(self.output)
        while counter < len(self.output):
            line = ""
            if len(self.output) - counter < cols:
                cols = len(self.output) - counter
            for i in range(cols):
                word = self.output[counter].ljust(space, " ")
                phrase = f"{str(i).rjust(3, '0')}. {word}  "
                line += phrase
                counter += 1
            print(line)
        return True

    def contains(self, val, count, length):
        inp = self.sanatize(val)
        count = -1 if not count else int(count)
        for _, word in enumerate(self.all_words):
            if count == 0:
                break
            if length and len(word) != int(length):
                continue
            if len([part for part in inp if part in word]) == len(inp):
                self.output.append(word)
                count -= 1
        if self.output:
            return self.show()
        return True

    def synonyms(self, val, count, length):
        pass

    def start(self, val, count, length):
        inp = "".join(self.sanatize(val))
        count = -1 if not count else int(count)
        for _, word in enumerate(self.all_words):
            if not count: break
            if length and len(word) != int(length):
                continue
            if word.startswith(inp):
                self.output.append(word)
                count -= 1
        if self.output:
            return self.show()
        return True

    def end(self, val, count, length):
        inp = "".join(self.sanatize(val))
        count = -1 if not count else int(count)
        for _, word in enumerate(self.all_words):
            if not count: break
            if length and len(word) != int(length):
                continue
            if word.endswith(inp) == len(inp):
                self.output.append(word)
                count -= 1
        if self.output:
            return self.show()
        return True


def binprint(args):
    value = int(args.value)
    print(bin(value)[2:])
