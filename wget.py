import os,sys,requests

if len(sys.argv) > 1:
    url = str(sys.argv[1])
else:
    print("Usage: `wget <url to file>`")
    quit()

x = url.split("/")
saveto = str(x[-1])

obj = requests.get(url)
f = open("home/"+saveto,'w')
f.write(obj.text)
f.close()
