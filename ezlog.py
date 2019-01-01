import sys,os

from oslib import hostmgr
h = hostmgr()

def verify(path):
    if os.path.exists(path):
        return True
    else:
        return False

if __name__ == "__main__":
    quit()

class ezlog:
    def __init__(self,programname):
        if not verify('..'+h.get()+'log'+h.get()+'ext'+h.get()+programname):
            os.makedirs('..'+h.get()+'log'+h.get()+'ext'+h.get()+programname)
        self.path = '..'+h.get()+'log'+h.get()'ext'+h.get()+programname
    def log(text):
        f = open(self.path,'a+')
        f.write("\n"+text)
        f.close()
