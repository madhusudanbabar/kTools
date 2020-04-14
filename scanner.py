#!/bin/python3

# impports
import sys
import socket
from datetime import datetime

#check args else throw error
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1]) # get ip of site
    except:
        print("failed to retrive ip address")
        sys.exit()

else:
    print("invalid number of args")
    print("Usage: "+ sys.argv[0] +" <ip>")
    sys.exit()

#here comes UI part
print("-"*50)
print("scanning target" +target)
print("Time started " +str(datetime.now()))
print("-"*50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("port {} is open".format(port))
            s.close()


except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

except socket.gaierror:
    print("hostname not found")
    sys.exit()

except socket.error:
    print("server not found")
    sys.exit()

