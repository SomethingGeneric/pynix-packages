import sys,os

def clear():
    print("\n"*200)

user = str(sys.argv[1])
if len(sys.argv) == 2:
    path = str(sys.argv[2])
else:
    print("Usage: less <filename>")
    
goal = 'home/'+user+"/"+path
# Because of the above lines, less is purposefully limited to the user's directory

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
