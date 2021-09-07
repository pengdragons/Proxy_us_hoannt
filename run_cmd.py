
import threading
import os
import sys

if len(sys.argv) != 2:
    print ("Usage: python %s <number_proxy>" % sys.argv[0])
    print ("Example: python %s 10" % sys.argv[0])
    raise SystemExit

try:
    number_proxy = int(sys.argv[1])
except:
    print ("Invalid number proxy")
    raise SystemExit

def ping_url(number):

    os.system(number)
f = open("port.txt", "r")
PORT = f.read()
thread_list = []
commands = []
for i in range(number_proxy):
    PORT = int(str(PORT)) - 1
    commands.append(str('proxybroker serve --host 2001:19f0:6001:10f5:5400:03ff:fe81:856d --port '+str(PORT) + ' --types HTTP HTTPS --lvl High -c US MAX_CONN 5'))

for url in commands:

    t = threading.Thread(target=ping_url, args=(url,))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Done")




