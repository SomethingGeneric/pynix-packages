import os

text = '''
PyNix help:
----------
pynSh built in commands:
exit
----------
Commands from bin:'''

lsbin = str(os.listdir('bin'))
lsbin = lsbin.replace("[","").replace("]","").replace("'","").replace(".py","").replace(",","\n")

text = text + "\n" + lsbin

print(text)
