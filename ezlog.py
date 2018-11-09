import sys,os

def verify(path):
    if os.path.exists(path):
        return True
    else:
        return False

if __name__ == "__main__":
    quit()

class ezlog:
    def __init__(self,programname):
        if not verify('..\\log\\ext\\'+programname):
            os.makedirs('..\\log\\ext\\'+programname)
        self.path = '..\\log\\ext\\'+programname
    def log(text):
        f = open(self.path,'a+')
        f.write("\n"+text)
        f.close()
