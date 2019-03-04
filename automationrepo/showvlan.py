#!/usr/bin/env python

from __future__ import print_function, unicode_literals

with open("showvlan.txt") as vlanfile:
    Vlan = vlanfile.readlines()[2:]
    Vlan.pop(1)
    
vlist = []

for name in Vlan:
    virtuallan = name.split()
    VLANid = virtuallan[0]
    VLANname = virtuallan[1]
    vlist.append((VLANid, VLANname))


print (vlist)

