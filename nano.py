import os,sys

user = str(sys.argv[1])
if len(sys.argv) == 2:
    path = str(sys.argv[2])
else:
    print("Usage: nano <filename>")
    quit()

goal = 'home\\'+user+"\\"+path
# Because of the above lines, Nano is purposefully limited to the user's directory

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
