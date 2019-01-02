import os,shutil,sys,requests

from oslib import hostmgr
h = hostmgr()

def verify(path):
    if os.path.exists(path):
        return 1
    else:
        return 0

command = str(sys.argv[1])
package = str(sys.argv[2])
if len(sys.argv) == 4:
    opt = str(sys.argv[3])
else:
    opt = ""

base = "https://somethinggeneric.github.io/pn-apt-packages/"
pfn = package + ".py"

if command == "install":
    r = requests.get(base + pfn)
    if not "<!DOCTYPE html>" in r.text:
        if not verify("bin"+h.get()+pfn:
            f = open("bin"+h.get()+pfn,"w+")
            f.write(r.text)
            f.close()
        else:
            print("Already installed. Use 'apt remove' first.")
    else:
        print("Package not found.")
elif command == "remove":
    if os.path.exists('bin'+h.get()+pfn):
        os.remove('bin'+h.get()+pfn)
        print("Removed " + package)
