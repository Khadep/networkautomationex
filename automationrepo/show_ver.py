#!/usr/bin/env python
"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.
Your output should look as follows:
          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102
"""
from __future__ import print_function, unicode_literals

with open("showversion.txt") as text:
    showver = text.readlines()

found1 = False
found2 = False
found3 = False

for line in showver:
    if "IOS" in line:
        versionpart = line.split(",")[2]
        version = versionpart.split()[1]
        found1 = True
    elif "*0" in line:
        serial  = line.split()[2]
        found2 = True
    elif "Configuration register" in line:
        config = line.split()[3]
        found3 = True
    if found1 and found2 and found3:
            print ("OS Version: " + version  + "\n Serial Number: " + serial + " \n Config Register: " + config)
            break

    

