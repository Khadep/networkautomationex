#!/usr/bin/env python

from __future__ import print_function, unicode_literals



""" turn the file into a list  of lines. split the lines and initiate (ip_addr) and mac_addr iinto vartiables

for loop that searches for the ip 10.220.88.1 if its found Print Default Gateway IP/MAC aL and the correspoinding ip and mac

also search for 10.220.88.30   print Arista3 IP/MAC and corresponding attributes

once both are found break out of the loop """

with open("show_arp.txt") as showarp:
    show_arp = showarp.readlines()

found1, found2 = (False, False)

for line in show_arp:
    items = line.split()
    ip_addr = items[1]
    mac_addr = items[3]

    if ip_addr == "10.220.88.1":
        print ("Default Dateway IP/MAC: " + (ip_addr) + " Mac Address: " + (mac_addr))
        found1 = True
    elif ip_addr == "10.220.88.30":
        print ("Arista3 IP/MAC: " + (ip_addr) + " Mac Address: " + (mac_addr))
        found2 = True

    if found1 and found2:
            print ("Exit")
            break
        