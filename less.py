import sys,os

from oslib import hostmgr
h = hostmgr()

def clear():
    print("\n"*200)


if len(sys.argv) == 2:
    path = str(sys.argv[1])
else:
    print("Usage: less <filename>")
    quit()

goal = 'home'+h.get()+path


f = open(goal)
text = f.read()
f.close()
lines = text.split("\n")
c = 0
max = len(lines)+1

while c != max:
    clear()
    his = c
    cnt = 0
    while cnt != his:
        print(str(lines[cnt]))
        cnt += 1
    input(":")
    c += 1
