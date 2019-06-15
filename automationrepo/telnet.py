#!/usr/bin/env python

import pdb
from  telnetlib import Telnet

pdb.set_trace()

def testtelnet():
    kp = Telnet('69.251.157.111', 5013)
    response = kp.read_until("#", timeout=120)
    if "#" in response :
        kp.write("reload " + "\r\n")
        Output1 = kp.read_until("#      " or "]",timeout=10)
        print Output1
        if 'confirm' in Output1:
            kp.write("\r\n")
            print "We just Rebooted"    


pdb.run(testtelnet())
