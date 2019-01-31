#!/usr/bin/env python
from scapy.all import *
import subprocess
import sys
from datetime import datetime as dtime

#MAC info for Dash Button
INFO_DASH_REDBULL='fc:65:de:07:71:e0'
WAKEUP_CMD='wakeonlan c8:cb:b8:c9:68:6d'

print("Dash button rebull start")

def arp_detect(pkt):
    if pkt.haslayer(ARP):
        if pkt[ARP].op == 1: #network request if pkt[ARP].hwsrc == INFO_DASH_REDBULL:
            if pkt[ARP].hwsrc == INFO_DASH_REDBULL:
                nowTime = dtime.now()
                print("Button detected! at %s" % nowTime.strftime("%Y-%m-%d %H:%M:%S"))
                process = subprocess.Popen(WAKEUP_CMD.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()

if __name__ == '__main__':
    print sniff(prn=arp_detect, filter="arp", store=0)
    print("Dash button rebull end")
    sys.exit()
