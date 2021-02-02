import os
import searcher as s
import sys
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Made:
    def __init__(self, c):
        self.me = c
    def change(self, variable):
        make = s.searcher(variable)
    def help():
        print("""
            -s, --search : Search the keyword.
            -p, --page: Page count.
            -c, --count: how many show list.
            --save, Save codes.
            -r, --read: Read the source code.

            examples:
                    ./sc.py -s code -c 1 -p 1
                    ./sc.py -s code -p 1 [Default: 10 count per page] OR ./sc.py -s
            """)
    def control(en):
        if en:
            return True
        else:
            return False
    def check(self, bom, search):
        order = ["-s", "--search", "-c", "--count", "-p", "--page"]
        for x in order:
            if x in bom:
                if search == x:
                    count = bom.index(x) + 1
                    teaser = bom[count]
                    return teaser
    def check_previous(self, bom):
        order = ["-s", "--search", "-c", "--count", "-p", "--page"]
        for x in order:
            if x in bom:
                return True
            else:
                return False
    def got(lord, loot):
        for m in loot:
            return lord.index(m)
    def command(self, com):
            ## bug when empty the arguments -s <space>
            if len(sys.argv) > 5:
                return print("Must be 5 Arguments not x > 3")
            if "-s" in com and "-c" in com and "-p":
                s.searcher.search(self, Made.check(self, com, "-s"), Made.check(self, com, "-p"))
                #s.searcher.stop("[INFO]: Firstly you need put search Keyword\nFor example: python3 searchcode.py -s [keyword] -c [keyword]")
            elif "-s" and "-p":
                s.searcher.search(self, Made.check(self, com, "-s"), Made.check(self, com, "-p"))
            else:
                print(f"{color.HEADER}[INFO]: {color.FAIL}You must use search(-s) keyword with count(-c)")
    def main(self):
        if len(sys.argv) == 1:
            Made.help()
        else:
            Made.command(self, sys.argv)
ma = Made("MaDe By 81l1nm1y0r")
ma.main()
