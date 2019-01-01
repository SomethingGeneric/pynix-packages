import os,sys

from oslib import hostmgr
h = hostmgr()


if len(sys.argv) == 2:
    path = str(sys.argv[1])
else:
    print("Usage: nano <filename>")
    quit()

goal = 'home'+h.get()+path


print("Editing file. Enter a blank line to exit and save.")

total = ""

while True:
    new = input(":")
    if new != "":
        total = total + "\n" + new
    else:
        break

f = open(goal,'w')
f.write(total)
f.close()
