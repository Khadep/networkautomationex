#!/usr/bin/env python

""" 
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items. """

with open("showlldpneighbors.txt") as lldp:
    lldpOUTPUT = lldp.readlines()

found1, found2 = (False, False)

for line in lldpOUTPUT:
    if "System Name:" in line:
        systemName = line.split()[2]
        found1 = True
    elif "Port id:" in line:
        portid = line.split()[2]
        found2 = True
    if found1 and found2:
        print (" System Name: " + (systemName) + " Port id:" + (portid))
        break
