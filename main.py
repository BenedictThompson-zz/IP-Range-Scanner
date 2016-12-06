import subprocess
import os
from threading import Thread
iptoping = raw_input("Please enter the ip you want to scan for (eg.10.100): ")
listofscanned =[]
def scanner(i):
    with open(os.devnull, "wb") as limbo:
        for k in xrange(i, 255):
            ipad = (iptoping + "." + str(k) + ".")
            for n in xrange(i, 255):
                    ip=(ipad + str(n))
                    if not ip in listofscanned:
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                stdout=limbo, stderr=limbo).wait()
                        if not result:
                                print ip, "is alive"

                        listofscanned.append(ip)
                        len(listofscanned)
for i in range(255):
    t = Thread(target=scanner, args=(i,))
    if 65025 > len(listofscanned):
        t.start()
    else:
        print ("DONE!")