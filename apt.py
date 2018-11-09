import os,shutil,sys,requests

command = str(sys.argv[1])
package = str(sys.argv[2])
if len(sys.argv) == 3:
    opt = str(sys.argv[3])
else:
    opt = ""

base = "https://raw.githubusercontent.com/SomethingGeneric/pynix-packages/master/"
pfn = package + ".py"

if command == "install":
    r = requests.get(base + pfn)
    if not os.path.exists(pfn):
        f = open(pfn,'w')
        f.write(r.text)
        f.close()
        print("Installed " + package)
    else:
        if opt == "f" or opt == "u":
            f = open(pfn,'w')
            f.write(r.text)
            f.close()
            print("Reinstalled/updated " + package)
        else:
            print("Package already installed. Use option 'f' to reinstall/update")
elif command == "remove":
    if os.path.exists(pfn):
        os.remove(pfn)
        print("Removed " + package)
