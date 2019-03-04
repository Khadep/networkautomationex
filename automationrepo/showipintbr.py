#!/usr/bin/env python

from __future__ import print_function, unicode_literals

with open("showipintbr.txt") as Y:
  X = Y.readlines()

  


for z in X: 
     
       
    r = z.split()

    
    

    if r[0] == "FastEthernet4" :
        interface = r[0] 
        ipadd = r[1]
        newtuple = (interface, ipadd)

        print (newtuple)

