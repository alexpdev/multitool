import sys
from multitool import execute

tests = [ "TRIC", "RIGG", "LLION", "PING",  "OLLE", "TROLL"]

def main():
    execute()

if __name__ == "__main__":
    for i in tests:
        sys.argv = ["multitool", "--count", "30", "--in", i]
        main()
