#!/usr/bin/env python

from __future__ import unicode_literals, print_function

khade = open("showversion.txt")

kp = khade.read();
print (kp)

print (type(kp))

khade.close()

with open("showversion.txt") as james:
    kp2 = james.readlines()
    print (kp2)
    print (type(kp2))