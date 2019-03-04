#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from pprint import pprint


with open("showarp.txt") as v:
   p = v.readlines()
l = (p[2::])
pprint(l)

def listsort(val):
    return val[1]

l.sort(key = listsort)

print (l)

k = (l[0:3])

print (k)

n = "\n"

n = n.join(k)
print (n)

with open("aprentries.txt", "w") as w:
    w.write(n);
