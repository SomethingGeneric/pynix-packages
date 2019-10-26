from oslib import hostmgr

h = hostmgr()

f = open("bin" + h.get() + "v.txt")
print(f.read())
f.close()
