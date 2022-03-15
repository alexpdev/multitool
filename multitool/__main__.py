import sys
from multitool.cli import execute

def main():
    execute()


tests = [ "TRIC", "RIGG", "LLION", "PING",  "OLLE", "TROLL"]

if __name__ == "__main__":
    for i in tests:
        sys.argv = ["multitool", "--count", "30", "--in", i]
        main()
