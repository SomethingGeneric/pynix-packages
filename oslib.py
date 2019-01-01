import os

def verify(path):
    if os.path.exists(path):
        return True
    else:
        return False

class hostmgr:
    def __init__(self):
        f = open("hostos")
        self.path = f.read()
        f.close()
    def get(self):
        return self.path


# from oslib import hostmgr
# h = hostmgr()
# useable_path = h.get()
