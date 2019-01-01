import os,shutil,sys,requests

from oslib import hostmgr
h = hostmgr()

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
    req = requests.get(base + package + ".txt")
    if os.path.exists(package+'.txt'):
        os.remove(package+'.txt')
    if not "404: Not Found" in req.text:
        f = open(package + ".txt",'w')
        os.system('python3 -m pip install -r ' + package + ".txt")
        os.remove(package+".txt")
    if not os.path.exists(pfn):
        f = open('bin'+h.get()+pfn,'w')
        f.write(r.text)
        f.close()
        print("Installed " + package)
    else:
        print("Package installed. If you're trying to update, use 'apt remove' first")
elif command == "remove":
    if os.path.exists('bin'+h.get()+pfn):
        os.remove('bin'+h.get()+pfn)
        print("Removed " + package)
