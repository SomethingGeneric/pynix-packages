import os,shutil,sys,requests

command = str(sys.argv[1])
package = str(sys.argv[2])
if len(sys.argv) == 4:
    opt = str(sys.argv[3])
else:
    opt = ""

base = "https://raw.githubusercontent.com/SomethingGeneric/pn-apt-packages/master/"
pfn = package + ".py"

if command == "install":
    r = requests.get(base + pfn)
    if not os.path.exists(pfn):
        f = open('bin/'+pfn,'w')
        f.write(r.text)
        f.close()
        print("Installed " + package)
    else:
        if opt == "f" or opt == "u":
            f = open('bin/'+pfn,'w')
            f.write(r.text)
            f.close()
            print("Reinstalled/updated " + package)
        else:
            print("Package already installed. Use option 'f' to reinstall/update")
elif command == "remove":
    if os.path.exists('bin/'+pfn):
        os.remove('bin/'+pfn)
        print("Removed " + package)
