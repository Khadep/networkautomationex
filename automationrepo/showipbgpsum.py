#!/usr/bin/env python

from __future__ import print_function, unicode_literals

with open("showipbgpsum.txt") as BGP:
    output = BGP.readlines()

first = output[0]
last = output[-1]


one= first.split()
two = last.split()

print ("Local ASN " + (one[-1]))
print ("Peer IP " + (two[0]))