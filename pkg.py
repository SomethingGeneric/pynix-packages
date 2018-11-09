import sys,os,requests

if len(sys.argv) > 1:
    action = str(sys.argv[1])
else:
    print("Need a command. Use either `get pkg`, `rem pkg`, or `upd pkg`")
    quit()
if len(sys.argv) > 2:
    name = str(sys.argv[2])

if action == "get":
    if not os.path.exists('bin/'+name+'.py'):
        obj = requests.get('https://mattcompton.me/pynix/'+name+".py")
        f = open('bin/'+name+'.py','w')
        f.write(obj.text)
        f.close()
elif action == "rem":
    os.remove('bin/'+name+'.py')
elif action == "upd":
    os.remove('bin/'+name+'.py')
    obj = requests.get('https://mattcompton.me/pynix/'+name+".py")
    f = open('bin/'+name+'.py','w')
    f.write(obj.text)
    f.close()
elif action == "upd-all":
    pkgs = os.listdir('bin')
    c = 0
    max = len(pkgs)
    while c != max:
        name = str(pkgs[c])
        os.remove('bin/'+name)
        obj = requests.get('https://mattcompton.me/pynix/'+name)
        f = open('bin/'+name,'w')
        f.write(obj.text)
        f.close()
        c += 1
