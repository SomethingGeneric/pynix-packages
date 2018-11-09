import os

username = input("User to change: ")
opass = input("Old password: ")
npass = input("New password: ")

f = open('sys\\acmgmt')
old = f.read()
f.close()
os.remove('sys\\acmgmt')
lines = old.split("\n")
max = len(lines)
c = 0
new = ""
while c != max:
    this = str(lines[c])
    if username in this:
        try:
            this = this.replace(opass,npass)
        except:
            print("Wrong current password.")
    new = new + "\n" + this
    c += 1
f = open('sys\\acmgmt','w')
f.write(new)
f.close()
print("All done!")
