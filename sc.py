import sys
import os
import searcher as search
import parser
import searcher

def help():
    print("""
    =======================INFO=========================
        -s, --search : Search the keyword.
        -p, --page: Page count.
        -c, --count: how many show list.
        --save, read code all lines and save.
        -r, --read: Read the source code.
        -u, --update: Updater.

        ========================usage=========================
                ./sc.py -s code -c 1 -p 1
                ./sc.py -s code -p 1 [Default: 10 count per page]
    """)
def check():
    if "-u" in sys.argv or "--update" in sys.argv:
        os.system("python3 update.py")
        sys.exit()
def main():
    save, read = False, False
    if len(sys.argv) == 1:
        help()
        return
    if "--save" in sys.argv:
        save = True
    if "--read" in sys.argv or "-r" in sys.argv:
        read = True
    commands = ["-s", "--search", "--page", "-p", "-c", "--count", "-r", "--read"]
    check()
    pars = parser.Parse(commands)
    args = pars.parse()
    bad = searcher.Search(args, save, read)
    bad.search()

main()
