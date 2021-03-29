
import glob
import os.path
import os
class color:
    HEADER = '[95m'
    OKBLUE = '[94m'
    OKCYAN = '[96m'
    OKGREEN = '[92m'
    WARNING = '[93m'
    FAIL = '[91m'
    ENDC = '[0m'
    BOLD = '[1m'
    UNDERLINE = '[4m'
got = os.system("pwd")
files = glob.glob(str(os.system("pwd")) + "/*")
for m in files:
    print(m)
for t in files:
    if os.path.basename(t) == "update.py":
        continue
    os.remove(t)
os.system("git clone --quiet https://github.com/QairexStudio/codeSearcher")
print(color.FAIL + "finished... " + color.ENDC + color.HEADER + "It is up to you whether or not to delete old files...." + color.ENDC)
