import os

def verify(path):
    if os.path.exists(path):
        return True
    else:
        return False

class hostmgr:
    def __init__(self):
        if not verify("hostos"):
            this = int(input("1) Windows\n2) MacOS/Unix"))
            if this == 1:
                save = "\\"
            elif this == 2:
                save = "/"
            else:
                save = "CANCEL"
            if save != "CANCEL":
                f = open("hostos",'w')
                f.write(save)
                f.close()
                self.path = save
            else:
                return "User entered invalid number."
        else:
            f = open("hostos")
            self.path = f.read()
            f.close()
    def get(self):
        return self.path


# from oslib import hostmgr
# h = hostmgr()
# useable_path = h.get()
