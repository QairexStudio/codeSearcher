import os
import json
import requests
import time
import sys
## Search code API v1 library
## Coded by 81l1nm1y0r from scratch
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
class searcher():
    def __init__(self, c):
        self.me = c
    def goes(self):
        return self.me
    def deletefile(fil):
        os.remove(fil)
    def readfile(my):
        with open(my, "r") as me:
            yield my.read()
    def writefile(file, text):
        with open(file, "w") as foo:
            foo.write(text)
    def appendfile(file, text):
        with open(file, "a") as kot:
            kot.write(text)
    def check(self, bom, search):
        order = ["-s", "--search", "-c", "--count", "-p", "--page"]
        for x in order:
            if x in bom:
                if search == x:
                    count = bom.index(x) + 1
                    teaser = bom[count]
                    return teaser
    def stop(ey):
        os.system("clear")
        print(ey)
    def parse_key(dir):
        result = dir["results"]
        for x in result:
            m = list(x.keys())
            return m
    def parse_values(self, dir, word):
        if "-s" in sys.argv and "-p" in sys.argv and len(sys.argv) == 5:
            for x in range(10):
                add = {}
                for m in range(10):
                    for bas in range(100):
                        req = requests.get("https://searchcode.com/api/codesearch_I/?q={0}&p={1}".format(searcher.check(self, sys.argv, "-s"), bas)).json()
                    add[searcher.parse_key(req)[m]] = req["results"][x][searcher.parse_key(req)[m]]
                    yield add
        else:
            for x in range(int(searcher.check(self, sys.argv, "-c"))):
                add = {}
                for m in range(10):
                    add[searcher.parse_key(dir)[m]] = dir["results"][x][searcher.parse_key(dir)[m]]
                    yield add
    def save_code(self, pars, valu):
        lot = valu.get("id")
        requ = requests.get("https://searchcode.com/api/result/{0}".format(lot))
        sot = json.loads(requ.text)["code"]
        bot = valu.get(pars)
        searcher.appendfile("code.txt", "{0} <==> {1}\n".format(pars, bot))
        searcher.appendfile("code.txt", "--------------Source Code-----------------------------\n{0}".format(sot))
    def check_rea(self, bom):
        if bom in sys.argv:
            return True
        else:
            return False
    def gui(self, parse, values):
        for m in parse:
            time.sleep(0.07)
            get = values.get(m)
            print(color.OKGREEN + "{0}".format(m) + color.ENDC + " <==> " + color.FAIL + color.BOLD + "{0}".format(get))
            if m == "filename":
                print(color.OKBLUE + color.BOLD + "----------------------------------------------------------------------------------------------------" + color.ENDC)
            if searcher.check_rea(self, "--save"):
                searcher.save_code(self, m, values)
                deletefile("code.txt")
    def write(self, word):
            #test = searcher.parse_key(word)[x]
            #val = searcher.parse_values(self, word, test)
            val = searcher.parse_values(self, word, 0)
                #searcher.gui(self, test, m)
            for m in val:
                searcher.gui(self, searcher.parse_key(word), m)
    def search(self, key, page):
        req = requests.get("https://searchcode.com/api/codesearch_I/?q={0}&p={1}".format(key, page))
        frame = json.loads(req.text)
        print(color.OKCYAN + "Search --> " + color.BOLD + "{0}".format(frame["matchterm"]))
        print(color.OKBLUE + color.BOLD + "----------------------------------------------------------------------------------------------------" + color.ENDC)
        searcher.write(self, frame)
