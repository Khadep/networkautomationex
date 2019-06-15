#!/usr/bin/env python
import pdb
from  telnetlib import Telnet



def reloadmultiple():
    List_of_IPs = [{'69.251.157.111': 5013}, {'69.251.157.111': 5006}, {'69.251.157.111': 5012}, {'69.251.157.111': 5010}]
    for item in List_of_IPs:
        
        for k, v in item.items():
            print v
            kp = Telnet(k, v)
            response = kp.read_until("#", timeout=120)
            if "#" in response :
                kp.write("reload " + "\r\n")
                Output1 = kp.read_until("#      " or "]",timeout=10)
                print Output1
                if 'confirm' in Output1:
                    kp.write("\r\n")
                    print "We just Rebooted" 
                else 
                    print "not sure why we cant hit the reboot prompt"   

reloadmultiple()
