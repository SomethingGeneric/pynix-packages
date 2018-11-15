import os,sys

<<<<<<< HEAD

if len(sys.argv) == 1:
    path = str(sys.argv[1])
else:
    print("Usage: nano <filename>")
    quit()
=======
user = str(sys.argv[1])
path = str(sys.argv[2])


>>>>>>> 7c9651f52af7d97d648a3fdc513683959ddf74c6

goal = 'home/'+path


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
