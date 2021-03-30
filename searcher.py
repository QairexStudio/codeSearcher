import os
import sys
import requests
import time
import re
import getpass
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Search:
    def __init__(self, datas, rescue, peruse):
        self.data = datas
        if rescue:
            self.save = rescue
        if peruse:
            self.peruse = peruse
    def analyze(self, data):
        na = data[0].split(".")
        with open(data[0], "r") as get:
            dat = get.read().lower()
            get = re.sub(na[0],"\033[91m" + na[0] + "\033[0m", dat)
            for hi in get:
                sys.stdout.flush()
                print(hi, end="")
                time.sleep(0.00100000)
            print("Coded By 81l1nm1y0r :P")
        #    get = re.finditer(filename, dat) ## GET INDEX
        #    for m in get:
        #        batter.append(m.span())
        #for k in range(len(batter)):
        #    for l in range(0, 2):
        #        print(batter[k][l])
    def fastly_read(self, data):
        na = data[0].split(".")
        with open(data[0], "r") as get:
            dat = get.read().lower()
            get = re.sub(na[0],"\033[91m" + na[0] + "\033[0m", dat)
            for hi in get:
                sys.stdout.flush()
                print(hi, end="")
            print("Coded By 81l1nm1y0r :P")
    def help():
        print("""
        =======================INFO=========================
            -s, --search : Search the keyword.
            -p, --page: Page count.
            -c, --count: how many show list.
            --save, read code all lines and save.
            -r, --read: Read the source code.
            -u, --update: Updater.

            ========================USAGE=========================
                    python3 sc.py -s code -c 1 -p 1
                    python3 sc.py -s code [10 count per page]
        """)
    def save(file, text):
        with open(file, "a") as ap:
            ap.write(text)
    def search(self):
        try:
            if self.peruse:
                while True:
                    select = input("(y)es or (n)o for FAST mode:")
                    if select.lower().startswith("y"):
                        Search.fastly_read(self, self.data)
                        return
                    else:
                        Search.analyze(self, self.data)
                        return
        except AttributeError:
            pass
        if self.data[0]:
            if len(self.data) == 1:
                Search.get_all(self)
        try:
            if int(self.data[1]) < int(self.data[2]):
                print("[ERROR] -p < -c")
                return
        except IndexError:
            pass
        try:
            req = requests.get("https://searchcode.com/api/codesearch_I/?q={0}&p={1}".format(str(self.data[0]), str(self.data[1]))).json()
            print(bcolors.WARNING + "Search -->", req["searchterm"])
            print("Total =>>", req["total"])
            print("Page =>>", req["total"] / 10)
            try:
                for m in range(0, int(self.data[2])):
                    for ka in req["results"][m]:
                        if ka == "url":
                            continue
                        print(ka + " ==> " + str(req["results"][m][ka]))
                        if ka == "filename":
                            if m == int(self.data[2]):
                                continue
                            print("-----------------------------------------------------------------------------------")
                        time.sleep(0.1000000000)
                    if self.save:
                        Search.save(str(self.data[0]) + ".txt", "---------------------------------{0}---------------------------------------\n".format(req["results"][m]["url"]) + requests.get("https://searchcode.com/api/result/{0}".format(str(req["results"][m]["id"]))).json()["code"] + "\n")
            except TypeError:
                print(bcolors.fail + "No result found!")
        except IndexError:
            pass
    def get_all(self):
        req = requests.get("https://searchcode.com/api/codesearch_I/?q={0}&p=0".format(str(self.data[0]))).json()
        hake = len(req["results"])
        print(bcolors.OKBLUE + "Search -->", req["searchterm"])
        print("Total =>>", req["total"])
        print("Page =>>", req["total"] / 10)
        for take in range(0, hake):
            for make in req["results"][take]:
                if make == "url":
                    continue
                print(make + " ==> " + str(req["results"][take][make]))
                if make == "filename":
                    print("-----------------------------------------------------------------------------------")
                time.sleep(0.1000000000)
            if self.save:
                Search.save(str(self.data[0]) + ".txt", "--------------------------------------{0}--------------------------------------\n".format(req["results"][take]["url"]) + requests.get("https://searchcode.com/api/result/{0}".format(str(req["results"][take]["id"]))).json()["code"] + "\n")
