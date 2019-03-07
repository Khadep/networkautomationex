#!/usr/bin/env python

from __future__ import print_function, unicode_literals


with open("intstatus998.txt") as switchoutput:
    text = switchoutput.readlines()

try:
    for line in text:
        eachline = line.split()
        if eachline[3] != "1000" and eachline[3] != "Unknown":
            print (" This AP port is not negotiating at 1Gbps : " + (eachline[0]))
except IndexError:
    eachline = "null"

     